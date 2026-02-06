import { ArrowRight, Github } from "lucide-react";
import { Link } from "react-router-dom";
import { Suspense, lazy } from "react";

const Scene3D = lazy(() => import("./Scene3D"));

const HeroSection = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center pt-32 overflow-hidden">
      {/* 3D Background */}
      <Suspense fallback={null}>
        <Scene3D />
      </Suspense>
      
      {/* Background Effects */}
      <div className="absolute inset-0 bg-grid opacity-20" />
      <div className="absolute inset-0 bg-radial-gradient" />
      
      {/* Floating Orbs - Now in red */}
      <div className="absolute top-1/4 left-1/4 w-72 h-72 bg-primary/30 rounded-full blur-[100px] animate-pulse-glow" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-secondary/30 rounded-full blur-[120px] animate-pulse-glow" />
      <div className="absolute top-1/2 right-1/3 w-64 h-64 bg-accent/20 rounded-full blur-[80px] animate-pulse-glow" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        {/* Main Headline */}
        <h1 className="heading-hero mb-6">
          Transform Your{" "}
          <span className="gradient-text">GitHub Repository</span>
          <br />
          Into Professional Docs
        </h1>

        {/* Subheadline */}
        <p className="text-body max-w-2xl mx-auto mb-10">
          Git2Doc uses advanced AI to analyze your codebase and generate comprehensive, 
          beautifully formatted PDF documentation in seconds. No more manual doc writing.
        </p>

        {/* CTA Button */}
        <div className="flex items-center justify-center mb-16">
          <Link to="/dashboard" className="btn-primary text-lg px-8 py-4 glow-primary">
            <Github className="w-5 h-5" /> Start Free <ArrowRight className="w-5 h-5" />
          </Link>
        </div>

        {/* Hero Image/Mockup */}
        <div className="relative max-w-4xl mx-auto">
          <div className="gradient-border p-1 rounded-2xl glow-primary">
            <div className="bg-card rounded-xl overflow-hidden">
              {/* Browser Chrome */}
              <div className="flex items-center gap-2 px-4 py-3 bg-muted border-b border-border">
                <div className="flex gap-2">
                  <div className="w-3 h-3 rounded-full bg-red-500/80" />
                  <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                  <div className="w-3 h-3 rounded-full bg-green-500/80" />
                </div>
                <div className="flex-1 mx-4">
                  <div className="bg-background/50 rounded-lg px-4 py-1.5 text-sm text-muted-foreground font-mono">
                    github.com/your-awesome-project
                  </div>
                </div>
              </div>
              
              {/* Content Preview */}
              <div className="p-8 bg-gradient-to-b from-card to-background">
                <div className="flex items-start gap-8">
                  {/* Code Preview */}
                  <div className="flex-1 text-left">
                    <div className="flex items-center gap-2 mb-4">
                      <Github className="w-5 h-5 text-muted-foreground" />
                      <span className="text-sm text-muted-foreground font-mono">Repository Analysis</span>
                    </div>
                    <div className="space-y-2 font-mono text-sm">
                      <div className="flex gap-2">
                        <span className="text-muted-foreground">├──</span>
                        <span className="text-primary">src/</span>
                      </div>
                      <div className="flex gap-2 pl-4">
                        <span className="text-muted-foreground">├──</span>
                        <span className="text-foreground">components/</span>
                      </div>
                      <div className="flex gap-2 pl-4">
                        <span className="text-muted-foreground">├──</span>
                        <span className="text-foreground">utils/</span>
                      </div>
                      <div className="flex gap-2">
                        <span className="text-muted-foreground">├──</span>
                        <span className="text-accent-green">README.md</span>
                      </div>
                      <div className="flex gap-2">
                        <span className="text-muted-foreground">└──</span>
                        <span className="text-secondary">package.json</span>
                      </div>
                    </div>
                  </div>

                  {/* Arrow */}
                  <div className="flex items-center">
                    <div className="w-16 h-16 rounded-full bg-gradient-to-r from-primary to-secondary flex items-center justify-center animate-float">
                      <ArrowRight className="w-8 h-8 text-white" />
                    </div>
                  </div>

                  {/* PDF Preview */}
                  <div className="flex-1 text-left">
                    <div className="flex items-center gap-2 mb-4">
                      <div className="w-5 h-5 rounded bg-red-500/20 flex items-center justify-center">
                        <span className="text-xs font-bold text-red-400">PDF</span>
                      </div>
                      <span className="text-sm text-muted-foreground font-mono">Generated Documentation</span>
                    </div>
                    <div className="bg-muted/50 rounded-lg p-4 border border-border">
                      <div className="h-2 bg-foreground/20 rounded w-3/4 mb-3" />
                      <div className="h-2 bg-foreground/10 rounded w-full mb-2" />
                      <div className="h-2 bg-foreground/10 rounded w-5/6 mb-2" />
                      <div className="h-2 bg-foreground/10 rounded w-4/5 mb-4" />
                      <div className="h-2 bg-primary/30 rounded w-1/2 mb-2" />
                      <div className="h-2 bg-foreground/10 rounded w-full mb-2" />
                      <div className="h-2 bg-foreground/10 rounded w-3/4" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Trust Indicators */}
        <div className="mt-16">
          <p className="text-sm text-muted-foreground mb-4">Trusted by developers at</p>
          <div className="flex flex-wrap items-center justify-center gap-8 opacity-50">
            <span className="text-xl font-bold">Google</span>
            <span className="text-xl font-bold">Microsoft</span>
            <span className="text-xl font-bold">Meta</span>
            <span className="text-xl font-bold">Amazon</span>
            <span className="text-xl font-bold">Netflix</span>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
