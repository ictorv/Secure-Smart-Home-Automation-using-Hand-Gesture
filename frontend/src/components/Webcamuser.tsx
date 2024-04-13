"use client";
import axios from "axios";
import Link from "next/link";
import { useCallback, useRef, useState } from "react"; // import useCallback
import Webcam from "react-webcam";
import { Button } from "./ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "./ui/card";
const Webcamuser = () => {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);

  // create a capture function
  const capture = useCallback(async () => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot();
      setImgSrc(imageSrc);
      console.log(imageSrc);
      const encodedString = encodeURIComponent(imageSrc);
      // console.log(encodedString);

      try {
        const response = await axios.get(
          `http://127.0.0.1:8001/upload-image-base/?base64_str=${encodedString}`
        );
        alert(response.data);
        // setLoading(false);
        // if (response.data.message === "matched!") {
        //   // setVerify("image matched! You're verified!");
        // } else {
        //   // setVerify("image not matched! You're not verified!");
        // }
      } catch (error) {
        console.error("Error:", error);
        // setVerify("face not captured properly");
      }
    }
  }, [webcamRef]);
  const notify = () => {
    alert("image captured|");
  };

  const handleCapture = () => {
    capture();
    notify();
  };
  return (
    <Card>
      <CardHeader>
        <CardTitle>Click click</CardTitle>
        <CardDescription>Take your photo!</CardDescription>
      </CardHeader>
      <CardContent className="space-y-2">
        {imgSrc ? (
          <>
            <img
              src={imgSrc}
              alt="webcam"
              className="border-green-400 border-4"
            />
            <CardFooter className="flex flex-col space-y-5 items-center justify-center">
              <Button>Image captured!</Button>
              <p>
                Go back to{" "}
                <Link href="/" className="underline">
                  login
                </Link>
              </p>
            </CardFooter>
          </>
        ) : (
          <>
            <Webcam
              height={400}
              width={400}
              ref={webcamRef}
              className="border-primary border-4 rounded-lg"
            />{" "}
            <CardFooter className="flex items-center justify-center">
              <Button onClick={handleCapture}>Capture photo</Button>
            </CardFooter>
          </>
        )}
      </CardContent>
    </Card>
  );
};

export default Webcamuser;
