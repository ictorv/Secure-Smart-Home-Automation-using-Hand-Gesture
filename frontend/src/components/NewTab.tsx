"use client";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import Register from "./Register";
import Webcamuser from "./Webcamuser";

export function NewTab() {
  return (
    <Tabs defaultValue="account" className="w-[400px] ">
      <TabsList className="grid w-full grid-cols-2 bg-slate-400">
        <TabsTrigger value="account">Register</TabsTrigger>
        <TabsTrigger value="password">Snap</TabsTrigger>
      </TabsList>
      <TabsContent value="account">
        <Register />
      </TabsContent>
      <TabsContent value="password">
        <Webcamuser />
      </TabsContent>
    </Tabs>
  );
}
