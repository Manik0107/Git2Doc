import { Github, Cpu, FileDown, ArrowRight } from "lucide-react";

const steps = [
  {
    number: "01",
    icon: Github,
    title: "Connect Your Repository",
    description: "Paste your GitHub repository URL or connect your GitHub account to import any public or private repo instantly.",
    color: "primary",
  },
  {
    number: "02",
    icon: Cpu,
    title: "AI Analyzes Your Code",
    description: "Our advanced AI scans your entire codebase, understanding the architecture, functions, APIs, and relationships between files.",
    color: "secondary",
  },
  {
    number: "03",
    icon: FileDown,
    title: "Download Your Documentation",
    description: "Get a beautifully formatted PDF with API references, architecture diagrams, code explanations, and more.",
    color: "accent-pink",
  },
];

const HowItWorksSection = () => {
  return (
    <section id="how-it-works" className="py-24 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-primary font-semibold text-sm uppercase tracking-wider">How It Works</span>
          <h2 className="heading-section mt-4">
            From Repository to Documentation
            <br />
            <span className="gradient-text">In Three Simple Steps</span>
          </h2>
        </div>

        {/* Steps */}
        <div className="relative">
          {/* Connection Line */}
          <div className="hidden lg:block absolute top-1/2 left-0 right-0 h-0.5 bg-gradient-to-r from-primary via-secondary to-accent-pink transform -translate-y-1/2" />

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {steps.map((step, index) => (
              <div key={step.number} className="relative">
                {/* Card */}
                <div className="card-glass p-8 h-full hover:border-primary hover:bg-primary/10 hover:shadow-lg hover:shadow-primary/20 transition-all duration-300 group">
                  {/* Step Number */}
                  <div className="flex items-center justify-between mb-6">
                    <span className="text-6xl font-black text-muted/50 group-hover:text-primary transition-colors duration-300">
                      {step.number}
                    </span>
                    <div className={`w-14 h-14 rounded-xl bg-${step.color}/10 flex items-center justify-center`}>
                      <step.icon className={`w-7 h-7 text-${step.color === 'accent-pink' ? 'accent-pink' : step.color}`} />
                    </div>
                  </div>

                  {/* Content */}
                  <h3 className="heading-card mb-4">{step.title}</h3>
                  <p className="text-body">{step.description}</p>

                  {/* Arrow for non-last items */}
                  {index < steps.length - 1 && (
                    <div className="hidden lg:flex absolute -right-4 top-1/2 transform -translate-y-1/2 z-10">
                      <div className="w-8 h-8 rounded-full bg-background border border-border flex items-center justify-center">
                        <ArrowRight className="w-4 h-4 text-muted-foreground" />
                      </div>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Demo CTA */}
        <div className="text-center mt-16">
          <p className="text-muted-foreground mb-4">See it in action</p>
          <a href="#preview" className="btn-primary">
            View Sample Output <ArrowRight className="w-4 h-4" />
          </a>
        </div>
      </div>
    </section>
  );
};

export default HowItWorksSection;
