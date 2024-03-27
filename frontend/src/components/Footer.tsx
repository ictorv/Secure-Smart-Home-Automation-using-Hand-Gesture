import { ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable";

export function Footer() {
  return (
    <ResizablePanelGroup
      direction="vertical"
      className="min-h-[100px] max-w-full rounded-lg border bg-gradient-to-r from-slate-800 to-slate-950 text-white text-sm sm:text-base"
    >
      <ResizablePanel>
        <div className="flex h-full items-center justify-center p-6">
          <span className="font-semibold">
            Illuminate your world with a flicker 🪔! Gesture-controlled
            appliances, lighting up your life with just a wave 🌟
          </span>
        </div>
      </ResizablePanel>
    </ResizablePanelGroup>
  );
}
