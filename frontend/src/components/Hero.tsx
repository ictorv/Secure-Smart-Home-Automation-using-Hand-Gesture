import { ProfileForm } from "./Profile-Form";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "./ui/resizable";

const Hero = () => {
  return (
    <div className="flex justify-center items-center m-8">
      <ResizablePanelGroup
        direction="horizontal"
        className="max-h-min max-w-fit rounded-lg border"
      >
        {/* <ResizablePanel defaultSize={50}>
      <div className="flex h-full items-center justify-center p-6">
        <ProfileForm />
      </div>
    </ResizablePanel> */}
        {/* <ResizableHandle /> */}
        <ResizablePanel defaultSize={50}>
          <ProfileForm />
        </ResizablePanel>
        <ResizableHandle />
      </ResizablePanelGroup>
    </div>
  );
};

export default Hero;
