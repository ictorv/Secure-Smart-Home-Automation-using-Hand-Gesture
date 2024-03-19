"use client";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import { InputOTPForm } from "./OTP-from";
import { ProfileForm } from "./Profile-Form";

export function Body() {
  const [image, setImage] = useState(""); // Define image state
  const webcamRef = useRef(null);

  const videoConstraints = {
    width: 200,
    height: 180,
    facingMode: "user", // or "environment" for rear camera
  };

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current?.getScreenshot();
    if (imageSrc) {
      setImage(imageSrc);
    }
  }, [webcamRef]);

  return (
    <ResizablePanelGroup
      direction="horizontal"
      className="min-h-[340px] max-w-full rounded-lg border"
    >
      <ResizablePanel defaultSize={33}>
        <div className="flex h-full items-center justify-center p-6">
          <ProfileForm />
        </div>
      </ResizablePanel>
      <ResizableHandle />
      <ResizablePanel defaultSize={33}>
        <div className="flex h-full items-center justify-center p-6">
          <div className="relative w-full">
            {image === "" ? (
              <Webcam
                audio={false}
                className="w-full"
                height={200}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={220}
                videoConstraints={videoConstraints}
              />
            ) : (
              <img src={image} className="w-full" alt="Captured" />
            )}
            {image !== "" && (
              <button
                onClick={(e) => {
                  e.preventDefault();
                  setImage("");
                }}
                className="absolute border-4 rounded-md p-1 border-primary text-primary bottom-5 left-5 z-10 btnShadow"
              >
                Retake
              </button>
            )}
            {image === "" && (
              <button
                onClick={(e) => {
                  e.preventDefault();
                  capture();
                }}
                className="absolute bg-transparent border-4 rounded-md p-1 border-primary text-primary bottom-5 left-5 z-10 btnShadow"
              >
                Capture
              </button>
            )}
          </div>
        </div>
      </ResizablePanel>
      <ResizableHandle />
      <ResizablePanel defaultSize={33}>
        <div className="flex h-full items-center justify-center p-6">
          <InputOTPForm />
        </div>
      </ResizablePanel>
    </ResizablePanelGroup>
  );
}
