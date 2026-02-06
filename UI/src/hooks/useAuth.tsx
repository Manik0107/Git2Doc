import { createContext, useContext, useState, useEffect, ReactNode } from "react";
import authService, { User as ApiUser } from "../services/authService";

interface User {
  id: number;
  fullName: string;
  email?: string | null;
  phone?: string | null;
  isAdmin: boolean;
}

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<{ success: boolean; error?: string }>;
  loginWithPhone: (phone: string) => Promise<{ success: boolean; error?: string }>;
  signup: (fullName: string, email: string, password: string) => Promise<{ success: boolean; error?: string }>;
  signupWithPhone: (fullName: string, phone: string) => Promise<{ success: boolean; error?: string }>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

const TOKEN_KEY = "token";
const USER_KEY = "user";

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Restore session on mount
  useEffect(() => {
    const restoreSession = async () => {
      const token = localStorage.getItem(TOKEN_KEY);
      const storedUser = localStorage.getItem(USER_KEY);

      if (token && storedUser) {
        try {
          // Verify token is still valid
          const currentUser = await authService.getMe();
          setUser({
            id: currentUser.id,
            fullName: currentUser.full_name,
            email: currentUser.email,
            phone: currentUser.phone,
            isAdmin: currentUser.is_admin,
          });
        } catch (error) {
          // Token invalid, clear storage
          localStorage.removeItem(TOKEN_KEY);
          localStorage.removeItem(USER_KEY);
        }
      }
      setIsLoading(false);
    };

    restoreSession();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const response = await authService.login(email, password);

      // Store token
      localStorage.setItem(TOKEN_KEY, response.access_token);
      console.log('✅ Token stored:', response.access_token.substring(0, 20) + '...');

      // Set user
      const userData: User = {
        id: response.user.id,
        fullName: response.user.full_name,
        email: response.user.email,
        phone: response.user.phone,
        isAdmin: response.user.is_admin,
      };

      setUser(userData);
      localStorage.setItem(USER_KEY, JSON.stringify(userData));
      console.log('✅ User set:', userData);

      return { success: true };
    } catch (error: any) {
      console.error('❌ Login error:', error);
      return {
        success: false,
        error: error.response?.data?.detail || "Login failed. Please check your credentials.",
      };
    }
  };

  const loginWithPhone = async (phone: string) => {
    try {
      const response = await authService.login(phone, "");

      // Store token
      localStorage.setItem(TOKEN_KEY, response.access_token);

      // Set user
      const userData: User = {
        id: response.user.id,
        fullName: response.user.full_name,
        email: response.user.email,
        phone: response.user.phone,
        isAdmin: response.user.is_admin,
      };

      setUser(userData);
      localStorage.setItem(USER_KEY, JSON.stringify(userData));

      return { success: true };
    } catch (error: any) {
      return {
        success: false,
        error: error.response?.data?.detail || "Phone number not registered"
      };
    }
  };

  const signup = async (fullName: string, email: string, password: string) => {
    try {
      const response = await authService.register({
        email,
        password,
        full_name: fullName,
      });

      // Store token
      localStorage.setItem(TOKEN_KEY, response.access_token);

      // Set user
      const userData: User = {
        id: response.user.id,
        fullName: response.user.full_name,
        email: response.user.email,
        phone: response.user.phone,
        isAdmin: response.user.is_admin,
      };

      setUser(userData);
      localStorage.setItem(USER_KEY, JSON.stringify(userData));

      return { success: true };
    } catch (error: any) {
      return {
        success: false,
        error: error.response?.data?.detail || "Email already registered"
      };
    }
  };

  const signupWithPhone = async (fullName: string, phone: string) => {
    try {
      const response = await authService.register({
        phone,
        full_name: fullName,
      });

      // Store token
      localStorage.setItem(TOKEN_KEY, response.access_token);

      // Set user
      const userData: User = {
        id: response.user.id,
        fullName: response.user.full_name,
        email: response.user.email,
        phone: response.user.phone,
        isAdmin: response.user.is_admin,
      };

      setUser(userData);
      localStorage.setItem(USER_KEY, JSON.stringify(userData));

      return { success: true };
    } catch (error: any) {
      return {
        success: false,
        error: error.response?.data?.detail || "Phone number already registered"
      };
    }
  };

  const logout = async () => {
    try {
      await authService.logout();
    } catch (error) {
      // Ignore errors on logout
    } finally {
      setUser(null);
      localStorage.removeItem(TOKEN_KEY);
      localStorage.removeItem(USER_KEY);
    }
  };

  return (
    <AuthContext.Provider value={{
      user,
      isAuthenticated: !!user,
      isLoading,
      login,
      loginWithPhone,
      signup,
      signupWithPhone,
      logout
    }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
