import apiClient from '@/lib/api';

export interface User {
    id: number;
    email: string | null;
    phone: string | null;
    full_name: string;
    is_admin: boolean;
    created_at: string;
}

export interface LoginResponse {
    access_token: string;
    token_type: string;
    user: User;
}

export interface RegisterData {
    email?: string;
    phone?: string;
    password?: string;
    full_name: string;
}

export interface LoginData {
    username: string; // email or phone
    password: string;
}

const authService = {
    async register(data: RegisterData): Promise<LoginResponse> {
        const response = await apiClient.post<LoginResponse>('/api/auth/register', data);
        return response.data;
    },

    async login(username: string, password: string): Promise<LoginResponse> {
        const formData = new URLSearchParams();
        formData.append('username', username);
        formData.append('password', password);

        const response = await apiClient.post<LoginResponse>('/api/auth/login', formData, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });
        return response.data;
    },

    async getMe(): Promise<User> {
        const response = await apiClient.get<User>('/api/auth/me');
        return response.data;
    },

    async logout(): Promise<void> {
        await apiClient.post('/api/auth/logout');
        localStorage.removeItem('token');
        localStorage.removeItem('user');
    },
};

export default authService;
