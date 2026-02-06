import Navbar from "@/components/codo/Navbar";
import PricingSection from "@/components/codo/PricingSection";
import FooterSection from "@/components/codo/FooterSection";

const Pricing = () => {
  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      <div className="pt-16">
        <PricingSection />
      </div>
      <FooterSection />
    </div>
  );
};

export default Pricing;
