import { Footer } from "@/components/Footer";
import { Header } from "@/components/Header";
import Hero from "@/components/Hero";

export default function Home() {
  return (
    <main className="max-h-lvh max-w-fit flex flex-col bg-gradient-to-r from-slate-800 to-slate-950 text-white text-sm sm:text-base">
      <Header />
      {/* <Body />
       */}
      <Hero />
      <Footer />
    </main>
  );
}
