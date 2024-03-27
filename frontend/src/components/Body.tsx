"use client";

import axios from "axios";
import { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";
import Loader from "./Loader";
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
      width: 200,
      height: 200,
    });
    setImage(imageSrc);
    console.log(imageSrc);
    const encodedString = encodeURIComponent(imageSrc);
    // console.log(encodedString);
    setLoading(true);

    try {
      const response = await axios.get(
        `http://127.0.0.1:8001/face-verification/?base64_str=${encodedString}`
      );
      alert(response.data.message);
      setLoading(false);
      if (response.data.message === "matched!") {
        setVerify("image matched! Session activated!");
      } else {
        setVerify("image not matched! You're not verified!");
      }
    } catch (error) {
      console.error("Error:", error);
      setVerify("face not captured properly");
    }
  }, [webcamRef]);

  return (
    <div className="flex flex-col h-full items-center justify-center p-6 max-h-screen">
      <div className="relative w-fit">
        {image === "" ? (
          <Webcam
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            audio={false}
            className="h-full"
            height={200}
            width={200}
            videoConstraints={videoConstraints}
          />
        ) : (
          <img src={image} height={200} width={200} alt="Captured" />
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
  );
}
