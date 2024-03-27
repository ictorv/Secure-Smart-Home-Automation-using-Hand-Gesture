"use client";
import { Footer } from "@/components/Footer";
import { Header } from "@/components/Header";
import { NewTab } from "@/components/NewTab";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "@/components/ui/resizable";
import React from "react";

const User: React.FC = () => {
  return (
    <main className="max-h-full max-w-fit flex flex-col bg-gradient-to-r from-slate-800 to-slate-950 text-white text-sm sm:text-base">
      <Header />
      <ResizablePanelGroup
        direction="horizontal"
        className=" rounded-lg border"
      >
        <ResizablePanel defaultSize={33}>
          <div className="flex h-full items-center justify-center p-6">
            docs
          </div>
        </ResizablePanel>
        <ResizableHandle />
        <ResizablePanel defaultSize={33}>
          <div className="flex h-full items-center justify-center p-6">
            {/* <Register />
             */}
            <NewTab />
          </div>
        </ResizablePanel>
      </ResizablePanelGroup>
      <Footer />
    </main>
  );
};

export default User;

// import { useRef, useState } from "react";

// const User: React.FC = () => {
//   const [verificationResult, setVerificationResult] = useState<string>("");
//   const videoRef = useRef<HTMLVideoElement>(null);
//   const canvasRef = useRef<HTMLCanvasElement>(null);

//   const startCamera = async () => {
//     try {
//       const stream = await navigator.mediaDevices.getUserMedia({ video: true });
//       if (videoRef.current) {
//         videoRef.current.srcObject = stream;
//       }
//     } catch (error) {
//       console.error("Error accessing webcam:", error);
//     }
//   };

//   const stopCamera = () => {
//     const stream = videoRef.current?.srcObject as MediaStream;
//     const tracks = stream?.getTracks();
//     tracks?.forEach((track) => track.stop());
//   };

//   const captureImage = () => {
//     if (videoRef.current && canvasRef.current) {
//       const canvas = canvasRef.current;
//       const video = videoRef.current;
//       canvas.width = video.videoWidth;
//       canvas.height = video.videoHeight;
//       canvas
//         .getContext("2d")
//         ?.drawImage(video, 0, 0, canvas.width, canvas.height);
//       const imageDataUrl = canvas.toDataURL("image/jpeg");
//       uploadImage(imageDataUrl);
//     }
//   };

//   const uploadImage = async (imageDataUrl: string) => {
//     const blob = await fetch(imageDataUrl).then((res) => res.blob());
//     const formData = new FormData();
//     formData.append("file", blob);

//     try {
//       const response = await axios.post(
//         "http://127.0.0.1:8000/image-verification/",
//         formData,
//         {
//           headers: {
//             "Content-Type": "multipart/form-data",
//           },
//         }
//       );
//       console.log(response.data.message);
//       setVerificationResult(response.data.message);
//     } catch (error) {
//       console.error("Error occurred during image verification:", error);
//       // Handle error accordingly
//     }
//   };

//   const handleVerify = () => {
//     if (!videoRef.current) return;
//     captureImage();
//   };

//   return (
//     <div>
//       <h2>Image Verification</h2>
//       <div>
//         <button className="border border-green-400" onClick={startCamera}>
//           Start Camera
//         </button>
//         <button className="border border-green-400" onClick={stopCamera}>
//           Stop Camera
//         </button>
//         <button className="border border-green-400" onClick={handleVerify}>
//           Verify Image
//         </button>
//       </div>
//       <video ref={videoRef} autoPlay muted />
//       <canvas ref={canvasRef} style={{ display: "none" }} />
//       {verificationResult && (
//         <div>
//           <h3 className="text-white">Verification Result:</h3>
//           <p className="text-white">{verificationResult}</p>
//         </div>
//       )}
//     </div>
//   );
// };

// export default User;
