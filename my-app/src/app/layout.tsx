import type { Metadata } from "next";
import { Press_Start_2P } from "next/font/google";
import "./globals.css";

const inter = Press_Start_2P({ weight: "400", subsets: ["cyrillic"] });

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}