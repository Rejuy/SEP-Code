import React from "react";
import { Navigate } from "react-router-dom";
import "../config";

export default function RequireAuth({ children }) {
  if (!global.config.isLogin) {
    return <Navigate to="/login" />;
  }
  return children;
}
