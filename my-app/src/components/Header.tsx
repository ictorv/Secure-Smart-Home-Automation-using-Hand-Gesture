import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";

export function Header() {
  return (
    <ResizablePanelGroup
      direction="vertical"
      className="min-h-[200px] max-w-full rounded-lg border"
    >
      <ResizablePanel defaultSize={45}>
        <div className="flex h-full items-center justify-center p-8 m-2">
          <h1 className="uppercase font-semibold text-4xl sm:text-5xl md:text-6xl lg:text-7xl">
            Vic<span className="text-blue-400">KS</span>
          </h1>
        </div>
      </ResizablePanel>
      <ResizableHandle />
      <ResizablePanel defaultSize={55}>
        <div className="flex h-full items-center justify-center p-6 m-3">
          <span className="font-semibold">
            Revolutionize home automation with our{" "}
            <span className="text-yellow-100">
              Raspberry Pi-based gesture detector
            </span>
            , empowering users to effortlessly control{" "}
            <span className="text-yellow-100">
              appliances with simple hand movements
            </span>
            .
          </span>
        </div>
      </ResizablePanel>
    </ResizablePanelGroup>
  );
}
