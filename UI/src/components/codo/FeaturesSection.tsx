import { 
  FileText, 
  GitBranch, 
  Clock, 
  Shield, 
  Zap, 
  Layout, 
  Code2, 
  BookOpen 
} from "lucide-react";

const features = [
  {
    icon: FileText,
    title: "Smart Documentation",
    description: "AI understands your code context to generate meaningful, human-readable documentation.",
  },
  {
    icon: GitBranch,
    title: "API Reference",
    description: "Automatically extract and document all your API endpoints, parameters, and responses.",
  },
  {
    icon: Layout,
    title: "Architecture Diagrams",
    description: "Visual diagrams showing component relationships and data flow in your application.",
  },
  {
    icon: Code2,
    title: "Code Explanations",
    description: "Clear explanations of complex functions and algorithms in plain English.",
  },
  {
    icon: Clock,
    title: "Document History",
    description: "Track all your generated documents and regenerate when your codebase changes.",
  },
  {
    icon: Shield,
    title: "Private & Secure",
    description: "Your code never leaves our secure servers. Enterprise-grade encryption.",
  },
  {
    icon: Zap,
    title: "Lightning Fast",
    description: "Generate complete documentation in seconds, not hours. Save weeks of work.",
  },
  {
    icon: BookOpen,
    title: "Multiple Formats",
    description: "Export to PDF, Markdown, or HTML. Perfect for any documentation needs.",
  },
];

const FeaturesSection = () => {
  return (
    <section id="features" className="py-24 relative bg-muted/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-secondary font-semibold text-sm uppercase tracking-wider">Features</span>
          <h2 className="heading-section mt-4">
            Everything You Need to
            <br />
            <span className="gradient-text">Document Your Code</span>
          </h2>
          <p className="text-body max-w-2xl mx-auto mt-4">
            Powerful features designed for developers who want professional documentation without the hassle.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {features.map((feature, index) => (
            <div
              key={feature.title}
              className="card-solid p-6 hover:border-primary/50 hover:shadow-lg hover:shadow-primary/5 transition-all duration-300 group"
            >
              <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-primary/20 to-secondary/20 flex items-center justify-center mb-4 group-hover:from-primary/30 group-hover:to-secondary/30 transition-all">
                <feature.icon className="w-6 h-6 text-primary" />
              </div>
              <h3 className="font-semibold text-lg mb-2">{feature.title}</h3>
              <p className="text-small">{feature.description}</p>
            </div>
          ))}
        </div>

        {/* Dashboard Preview */}
        <div className="mt-20">
          <div className="text-center mb-8">
            <h3 className="heading-card">
              Dashboard for <span className="gradient-text">Complete Control</span>
            </h3>
          </div>
          
          <div className="gradient-border p-1 rounded-2xl">
            <div className="bg-card rounded-xl overflow-hidden">
              {/* Dashboard Header */}
              <div className="flex items-center justify-between px-6 py-4 border-b border-border">
                <div className="flex items-center gap-4">
                  <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-secondary" />
                  <span className="font-semibold">Git2Doc Dashboard</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-full bg-muted" />
                </div>
              </div>

              {/* Dashboard Content */}
              <div className="p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
                {/* Stats */}
                <div className="col-span-1 md:col-span-3 grid grid-cols-3 gap-4">
                  <div className="bg-muted/50 rounded-lg p-4">
                    <p className="text-sm text-muted-foreground">Total Documents</p>
                    <p className="text-2xl font-bold">24</p>
                  </div>
                  <div className="bg-muted/50 rounded-lg p-4">
                    <p className="text-sm text-muted-foreground">Repositories</p>
                    <p className="text-2xl font-bold">8</p>
                  </div>
                  <div className="bg-muted/50 rounded-lg p-4">
                    <p className="text-sm text-muted-foreground">This Month</p>
                    <p className="text-2xl font-bold">12</p>
                  </div>
                </div>

                {/* Recent Documents */}
                <div className="col-span-1 md:col-span-2 bg-muted/30 rounded-lg p-4">
                  <h4 className="font-semibold mb-4">Recent Documents</h4>
                  <div className="space-y-3">
                    {[
                      { name: "react-dashboard-docs.pdf", repo: "react-dashboard", date: "2 hours ago" },
                      { name: "api-reference.pdf", repo: "backend-api", date: "Yesterday" },
                      { name: "component-library.pdf", repo: "ui-components", date: "3 days ago" },
                    ].map((doc) => (
                      <div key={doc.name} className="flex items-center justify-between bg-background/50 rounded-lg p-3">
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 rounded bg-red-500/20 flex items-center justify-center">
                            <FileText className="w-4 h-4 text-red-400" />
                          </div>
                          <div>
                            <p className="text-sm font-medium">{doc.name}</p>
                            <p className="text-xs text-muted-foreground">{doc.repo}</p>
                          </div>
                        </div>
                        <span className="text-xs text-muted-foreground">{doc.date}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Quick Actions */}
                <div className="bg-muted/30 rounded-lg p-4">
                  <h4 className="font-semibold mb-4">Quick Actions</h4>
                  <div className="space-y-2">
                    <button className="w-full btn-primary justify-center text-sm py-2">
                      New Document
                    </button>
                    <button className="w-full btn-outline justify-center text-sm py-2">
                      Connect Repo
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;
