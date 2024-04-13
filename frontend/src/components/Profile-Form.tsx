"use client";
import axios from "axios";
import Link from "next/link";
import React, { useState } from "react";
import { InputOTPForm } from "./OTP-from";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import {
  ResizableHandle,
  ResizablePanel,
  ResizablePanelGroup,
} from "./ui/resizable";
export function ProfileForm() {
  const [username, setUsername] = useState("");
  // const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(" ");
  const [success, setSuccess] = useState(false);
  const [otp, setOTP] = useState("");
  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    // setError(null);
    try {
      const response = await axios.post("http://127.0.0.1:8001/login/", {
        username: username,
        password: password,
      });
      setLoading(false);
      setSuccess(true);
      console.log("Response from server:", response.data);
      // Optionally, reset the form fields after successful submission
      setOTP(response.data.message);
      setUsername("");
      setPassword("");
    } catch (error: any) {
      alert(error);
      setError((error as { error: string }).error); // Assertion to access the 'error' property
      console.error("Error:", error);
    }
  };

  return (
    <ResizablePanelGroup
      direction="horizontal"
      className="min-h-[340px] max-w-full rounded-lg border"
    >
      <ResizablePanel defaultSize={30}>
        <Card className=" bg-slate-50 ">
          <CardHeader>
            <CardTitle>Login</CardTitle>
            {/* <CardDescription>
          Change your password here. After saving, you'll be logged out.
        </CardDescription> */}
          </CardHeader>
          <CardContent className="space-y-2 ">
            <div className="w-full max-h-max my-5 mx-auto">
              {success ? (
                <div className="w-full min-h-max">
                  <p>You are successfully logged in !</p>
                  <div className="flex justify-center items-center m-4">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="currentColor"
                      className="w-20 h-20 "
                    >
                      <path
                        fillRule="evenodd"
                        d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm4.28 10.28a.75.75 0 0 0 0-1.06l-3-3a.75.75 0 1 0-1.06 1.06l1.72 1.72H8.25a.75.75 0 0 0 0 1.5h5.69l-1.72 1.72a.75.75 0 1 0 1.06 1.06l3-3Z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </div>
                  <i className=" font-light text-sm text-gray-500">
                    To activate your session enter the otp sent to you email :)
                  </i>
                </div>
              ) : (
                <form
                  className="bg-slate-50 shadow-md border-t-primary border-t-4 rounded px-8 pt-6 pb-8 mb-4"
                  onSubmit={handleSubmit}
                >
                  <div className="mb-4">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="username"
                    >
                      Username
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="username"
                      type="text"
                      placeholder="Username"
                      value={username}
                      onChange={handleUsernameChange}
                      required
                    />
                  </div>

                  <div className="mb-6">
                    <label
                      className="block text-gray-700 text-sm font-bold mb-2"
                      htmlFor="password"
                    >
                      Password
                    </label>
                    <input
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                      id="password"
                      type="password"
                      placeholder="Password"
                      value={password}
                      onChange={handlePasswordChange}
                      required
                    />
                  </div>
                  <div className="flex flex-col items-center justify-between space-y-5">
                    <button
                      className=" bg-blue-500 hover:bg-blue-700  text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                      type="submit"
                      disabled={loading}
                    >
                      {loading ? "Loading..." : success ? "Success" : "Log In"}
                    </button>
                    {error && (
                      <p className="text-red-500 space-x-3 text-xs italic">
                        {error}
                      </p>
                    )}
                    <div className="flex justify-center items-center">
                      <p className="text-sm">
                        NOT Registered?
                        <Link className=" underline" href="/user">
                          Register as user
                        </Link>
                      </p>
                    </div>
                  </div>
                </form>
              )}
            </div>
          </CardContent>
        </Card>
      </ResizablePanel>
      <ResizableHandle />
      <ResizablePanel defaultSize={70}>
        <div className="flex h-full items-center justify-center p-6">
          <InputOTPForm otp={otp} />
        </div>
      </ResizablePanel>
    </ResizablePanelGroup>
  );
}
