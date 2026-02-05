import { Check } from "lucide-react";
import { Link } from "react-router-dom";

const plans = [
  {
    name: "Free",
    price: "$0",
    period: "forever",
    description: "Perfect for trying out Git2Doc on personal projects",
    features: [
      "3 documents per month",
      "Public repositories only",
      "Basic PDF export",
      "Standard processing",
      "Community support",
    ],
    cta: "Get Started Free",
    ctaVariant: "outline",
    highlighted: false,
  },
  {
    name: "Pro",
    price: "$19",
    period: "per month",
    description: "For developers who need unlimited documentation",
    features: [
      "Unlimited documents",
      "Public & private repositories",
      "PDF, Markdown & HTML export",
      "Priority processing",
      "Document history & versions",
      "API access",
      "Email support",
    ],
    cta: "Start Pro Trial",
    ctaVariant: "primary",
    highlighted: true,
  },
  {
    name: "Team",
    price: "$49",
    period: "per month",
    description: "Collaborate with your entire development team",
    features: [
      "Everything in Pro",
      "Up to 10 team members",
      "Shared document workspace",
      "Team analytics",
      "Custom branding",
      "SSO authentication",
      "Priority support",
    ],
    cta: "Contact Sales",
    ctaVariant: "outline",
    highlighted: false,
  },
];

const PricingSection = () => {
  return (
    <section id="pricing" className="py-24 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center mb-16">
          <span className="text-accent-pink font-semibold text-sm uppercase tracking-wider">Pricing</span>
          <h2 className="heading-section mt-4">
            Simple, Transparent
            <br />
            <span className="gradient-text">Pricing for Everyone</span>
          </h2>
          <p className="text-body max-w-2xl mx-auto mt-4">
            Start free, upgrade when you're ready. No hidden fees, no surprises.
          </p>
        </div>

        {/* Pricing Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {plans.map((plan) => (
            <div
              key={plan.name}
              className={`relative rounded-2xl p-8 transition-all duration-300 ${
                plan.highlighted
                  ? "gradient-border bg-card scale-105 shadow-2xl shadow-primary/20"
                  : "card-solid hover:border-border/80"
              }`}
            >
              {plan.highlighted && (
                <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                  <div className="bg-gradient-to-r from-primary to-secondary text-white text-xs font-semibold px-4 py-1 rounded-full flex items-center gap-1">
                    Most Popular
                  </div>
                </div>
              )}

              <div className="text-center mb-8">
                <h3 className="text-xl font-bold mb-2">{plan.name}</h3>
                <div className="flex items-baseline justify-center gap-1">
                  <span className="text-4xl font-black">{plan.price}</span>
                  <span className="text-muted-foreground">/{plan.period}</span>
                </div>
                <p className="text-small mt-2">{plan.description}</p>
              </div>

              <ul className="space-y-4 mb-8">
                {plan.features.map((feature) => (
                  <li key={feature} className="flex items-start gap-3">
                    <Check className="w-5 h-5 text-accent-green flex-shrink-0 mt-0.5" />
                    <span className="text-sm">{feature}</span>
                  </li>
                ))}
              </ul>

              <Link
                to="/signup"
                className={`w-full justify-center ${
                  plan.ctaVariant === "primary" ? "btn-primary" : "btn-outline"
                }`}
              >
                {plan.cta}
              </Link>
            </div>
          ))}
        </div>

        {/* FAQ Teaser */}
        <div className="text-center mt-16">
          <p className="text-muted-foreground">
            Have questions?{" "}
            <a href="#" className="text-primary hover:underline">
              Check our FAQ
            </a>{" "}
            or{" "}
            <a href="#" className="text-primary hover:underline">
              contact support
            </a>
          </p>
        </div>
      </div>
    </section>
  );
};

export default PricingSection;
