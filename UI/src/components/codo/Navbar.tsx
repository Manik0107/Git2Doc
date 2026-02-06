import { Link, useLocation } from "react-router-dom";
import { FileText, Menu, X, ChevronDown, User, LogOut } from "lucide-react";
import { useState } from "react";
import { useAuth } from "@/hooks/useAuth";

const Navbar = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [homeDropdownOpen, setHomeDropdownOpen] = useState(false);
  const [accountDropdownOpen, setAccountDropdownOpen] = useState(false);
  const location = useLocation();
  const { user, isAuthenticated, logout } = useAuth();

  const isHomePage = location.pathname === "/";

  const handleHomeLink = (hash: string) => {
    setHomeDropdownOpen(false);
    setMobileMenuOpen(false);
    if (isHomePage) {
      const element = document.querySelector(hash);
      element?.scrollIntoView({ behavior: "smooth" });
    } else {
      window.location.href = `/${hash}`;
    }
  };

  const handleLogout = () => {
    logout();
    setAccountDropdownOpen(false);
    setMobileMenuOpen(false);
  };

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-xl border-b border-border">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-secondary flex items-center justify-center">
              <FileText className="w-5 h-5 text-white" />
            </div>
            <span className="font-bold text-xl">Git2Doc</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-8">
            {/* Home Dropdown */}
            <div 
              className="relative"
              onMouseEnter={() => setHomeDropdownOpen(true)}
              onMouseLeave={() => setHomeDropdownOpen(false)}
            >
              <button
                className="flex items-center gap-1 text-muted-foreground hover:text-foreground transition-colors"
              >
                Home
                <ChevronDown className={`w-4 h-4 transition-transform ${homeDropdownOpen ? "rotate-180" : ""}`} />
              </button>
              {homeDropdownOpen && (
                <div className="absolute top-full left-0 pt-2">
                  <div className="w-48 bg-card border border-border rounded-lg shadow-xl py-2 z-50">
                    <button
                      onClick={() => handleHomeLink("#how-it-works")}
                      className="w-full text-left px-4 py-2 text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
                    >
                      How It Works
                    </button>
                    <button
                      onClick={() => handleHomeLink("#features")}
                      className="w-full text-left px-4 py-2 text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
                    >
                      Features
                    </button>
                    <button
                      onClick={() => handleHomeLink("#preview")}
                      className="w-full text-left px-4 py-2 text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
                    >
                      Preview
                    </button>
                  </div>
                </div>
              )}
            </div>
            <Link to="/pricing" className="text-muted-foreground hover:text-foreground transition-colors">
              Pricing
            </Link>
            <Link to="/dashboard" className="text-muted-foreground hover:text-foreground transition-colors">
              Dashboard
            </Link>
          </div>

          {/* Desktop Auth Buttons */}
          <div className="hidden md:flex items-center gap-3">
            {isAuthenticated ? (
              <div 
                className="relative"
                onMouseEnter={() => setAccountDropdownOpen(true)}
                onMouseLeave={() => setAccountDropdownOpen(false)}
              >
                <button
                  className="flex items-center gap-2 px-3 py-2 rounded-lg bg-muted hover:bg-muted/80 transition-colors"
                >
                  <div className="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center">
                    <User className="w-4 h-4 text-white" />
                  </div>
                  <span className="text-sm font-medium">{user?.fullName}</span>
                  <ChevronDown className={`w-4 h-4 transition-transform ${accountDropdownOpen ? "rotate-180" : ""}`} />
                </button>
                {accountDropdownOpen && (
                  <div className="absolute top-full right-0 pt-2">
                    <div className="w-48 bg-card border border-border rounded-lg shadow-xl py-2 z-50">
                      <div className="px-4 py-2 border-b border-border">
                        <p className="text-sm font-medium">{user?.fullName}</p>
                        <p className="text-xs text-muted-foreground">{user?.email || user?.phone}</p>
                      </div>
                      <Link
                        to="/dashboard"
                        className="block w-full text-left px-4 py-2 text-muted-foreground hover:text-foreground hover:bg-muted/50 transition-colors"
                        onClick={() => setAccountDropdownOpen(false)}
                      >
                        Dashboard
                      </Link>
                      <button
                        onClick={handleLogout}
                        className="w-full text-left px-4 py-2 text-red-400 hover:text-red-300 hover:bg-muted/50 transition-colors flex items-center gap-2"
                      >
                        <LogOut className="w-4 h-4" />
                        Log out
                      </button>
                    </div>
                  </div>
                )}
              </div>
            ) : (
              <Link to="/login" className="btn-ghost">
                Log in
              </Link>
            )}
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-border">
            <div className="flex flex-col gap-4">
              {/* Mobile Home Dropdown */}
              <div>
                <button
                  onClick={() => setHomeDropdownOpen(!homeDropdownOpen)}
                  className="flex items-center gap-1 text-muted-foreground hover:text-foreground transition-colors"
                >
                  Home
                  <ChevronDown className={`w-4 h-4 transition-transform ${homeDropdownOpen ? "rotate-180" : ""}`} />
                </button>
                {homeDropdownOpen && (
                  <div className="ml-4 mt-2 flex flex-col gap-2">
                    <button
                      onClick={() => handleHomeLink("#how-it-works")}
                      className="text-left text-muted-foreground hover:text-foreground transition-colors"
                    >
                      How It Works
                    </button>
                    <button
                      onClick={() => handleHomeLink("#features")}
                      className="text-left text-muted-foreground hover:text-foreground transition-colors"
                    >
                      Features
                    </button>
                    <button
                      onClick={() => handleHomeLink("#preview")}
                      className="text-left text-muted-foreground hover:text-foreground transition-colors"
                    >
                      Preview
                    </button>
                  </div>
                )}
              </div>
              <Link 
                to="/pricing" 
                className="text-muted-foreground hover:text-foreground transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                Pricing
              </Link>
              <Link 
                to="/dashboard" 
                className="text-muted-foreground hover:text-foreground transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                Dashboard
              </Link>
              <div className="flex flex-col gap-2 pt-4 border-t border-border">
                {isAuthenticated ? (
                  <>
                    <div className="flex items-center gap-2 px-2 py-2">
                      <div className="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center">
                        <User className="w-4 h-4 text-white" />
                      </div>
                      <div>
                        <p className="text-sm font-medium">{user?.fullName}</p>
                        <p className="text-xs text-muted-foreground">{user?.email || user?.phone}</p>
                      </div>
                    </div>
                    <button
                      onClick={handleLogout}
                      className="btn-outline justify-center text-red-400 border-red-400/30 hover:bg-red-400/10"
                    >
                      <LogOut className="w-4 h-4" />
                      Log out
                    </button>
                  </>
                ) : (
                  <Link to="/login" className="btn-outline justify-center" onClick={() => setMobileMenuOpen(false)}>
                    Log in
                  </Link>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
