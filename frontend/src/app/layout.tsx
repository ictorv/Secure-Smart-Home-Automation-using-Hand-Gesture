import type { Metadata } from "next";
import { Press_Start_2P } from "next/font/google";
import "./globals.css";

const inter = Press_Start_2P({ weight: "400", subsets: ["cyrillic"] });

export const metadata: Metadata = {
  title: "Vicks",
  description: "Developed @HITK",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <main className=" bg-gradient-to-r from-slate-800 to-slate-950 text-white text-sm sm:text-base">
          {/* <Header /> */}
          {children}
          {/* <Footer /> */}
        </main>
      </body>
    </html>
  );
}
