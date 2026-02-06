import { useEffect } from "react";
import Navbar from "@/components/codo/Navbar";
import HeroSection from "@/components/codo/HeroSection";
import HowItWorksSection from "@/components/codo/HowItWorksSection";
import FeaturesSection from "@/components/codo/FeaturesSection";
import SamplePreviewSection from "@/components/codo/SamplePreviewSection";
import FooterSection from "@/components/codo/FooterSection";

const Index = () => {
  useEffect(() => {
    window.scrollTo({ top: 0, left: 0, behavior: "instant" });
    if (window.location.hash) {
      window.history.replaceState(null, "", window.location.pathname);
    }
  }, []);
  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      <HeroSection />
      <HowItWorksSection />
      <FeaturesSection />
      <SamplePreviewSection />
      <FooterSection />
    </div>
  );
};

export default Index;
