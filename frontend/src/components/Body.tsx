"use client";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";

import axios from "axios";
import { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import Loader from "./Loader";
import { InputOTPForm } from "./OTP-from";
import { ProfileForm } from "./Profile-Form";
export function Body() {
  const webcamRef = useRef(null);
  const [loading, setLoading] = useState(false);
  const [image, setImage] = useState(""); // Define image state
  const [verify, setVerify] = useState("not-yet-verified");
  const videoConstraints = {
    facingMode: "user", // or "environment" for rear camera
  };

  const capture = useCallback(async () => {
    const imageSrc = webcamRef.current.getScreenshot({
      width: 500,
      height: 500,
    });
    setImage(imageSrc);
    console.log(imageSrc);
    const encodedString = encodeURIComponent(imageSrc);
    // console.log(encodedString);
    setLoading(true);
    // try {
    //   const response = await fetch(
    //     `http://127.0.0.1:8000/face-verification/?base64_str=${encodedString}`,

    //     {
    //       method: "GET",
    //       headers: {
    //         accept: "application/json",
    //       },
    //       mode: "no-cors",
    //     }
    //   );

    //   if (response.ok) {
    //     const data = await response.json();
    //     console.log(data.message);
    //     // setVerificationResult(data.message);
    //   } else {
    //     // Handle error response
    //     console.error(
    //       "Error occurred during api response:",
    //       response.statusText
    //     );
    //   }
    // } catch (error) {
    //   console.error("Error occurred during image matching:", error);
    //   // Handle error accordingly
    // }
    try {
      const response = await axios.get(
        `http://127.0.0.1:8001/face-verification/?base64_str=${encodedString}`
      );
      alert(response.data.message);
      setLoading(false);
      if (response.data.message === "matched!") {
        setVerify("image matched! You're verified!");
      } else {
        setVerify("image not matched! You're not verified!");
      }
    } catch (error) {
      console.error("Error:", error);
      setVerify("face not captured properly");
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
        {/* <div className="flex flex-col h-full items-center justify-center p-6">
          <div className="relative w-full">
            {image === "" ? (
              <Webcam
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                audio={false}
                className="w-full"
                height={200}
                width={220}
                videoConstraints={videoConstraints}
              />
            ) : (
              <img
                src={image}
                height={200}
                width={220}
                // className="w-full"
                alt="Captured"
              />
            )}
            {image !== "" && (
              <div className="relative">
                <img src={image} height={200} width={220} alt="Captured" />
                <button
                  onClick={(e) => {
                    e.preventDefault();
                    setImage("");
                  }}
                  className="absolute bottom-5 left-5 z-10 btnShadow bg-green-400 border-4 border-green-400 rounded-md p-1 text-accent"
                >
                  Retake
                </button>
                <div className="mt-5 space-y-10">
                  <p className="text-white mb-4">{verify}</p>
                </div>
              </div>
            )}

            {image === "" && (
              <button
                onClick={(e) => {
                  e.preventDefault();
                  capture();
                }}
                className="absolute bg-green-400 border-4 rounded-md p-1 border-green-400 text-accent bottom-5 left-5 z-10 btnShadow"
              >
                Capture
              </button>
            )}
          </div>
        </div> */}
        <div className="flex flex-col h-full items-center justify-center p-6">
          <div className="relative w-full">
            {image === "" ? (
              <Webcam
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                audio={false}
                className="w-full"
                height={200}
                width={220}
                videoConstraints={videoConstraints}
              />
            ) : (
              <img src={image} height={200} width={220} alt="Captured" />
            )}

            {image === "" && (
              <button
                onClick={(e) => {
                  e.preventDefault();
                  capture();
                }}
                className="absolute bg-green-400 border-4 rounded-md p-1 border-green-400 text-accent bottom-5 left-5 z-10 btnShadow"
              >
                Capture
              </button>
            )}
          </div>
          <div className="mt-5 space-y-10">{loading && <Loader />}</div>
          <div className="mt-5 space-y-10">
            <p className="text-white mb-4">{verify}</p>
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
