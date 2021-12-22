import { LockOutlined } from "@mui/icons-material";
import {
  Alert,
  Avatar,
  Box,
  Button,
  Snackbar,
  TextField,
  Typography,
} from "@mui/material";
import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../config";

export default function Login() {
  const navigate = useNavigate();
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  const [open, setOpen] = useState(false); // info tag
  const HandleLogin = () => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_login", {
        user_name: username,
        password: password,
      })
      .then((res) => {
        console.log(res);
        if (res.data.status === 0) {
          localStorage.setItem("secretCode", res.data.secret_code);
          navigate("/");
        } else {
          setOpen(true);
        }
      })
      .catch((err) => console.log(err));
  };
  const HandleClose = () => {
    setOpen(false);
  };

  return (
    <div className="container" style={{ height: "100%", width: "100%" }}>
      <Snackbar open={open} autoHideDuration={6000} onClose={HandleClose}>
        <Alert
          onClose={HandleClose}
          severity="error"
          sx={{
            width: "100%",
            fontSize: "20px",
            display: "flex",
            alignItems: "center",
          }}
        >
          登录失败
        </Alert>
      </Snackbar>
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlined />
        </Avatar>
        <Typography component="h1" variant="h5">
          管理员登录
        </Typography>
        <Box component="form" noValidate sx={{ mt: 1 }}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="username"
            label="用户名"
            name="adminUsername"
            onChange={(e) => {
              setusername(e.target.value);
            }}
            autoFocus
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="密码"
            type="password"
            id="password"
            onChange={(e) => {
              setpassword(e.target.value);
            }}
            autoComplete="current-password"
          />
          <Button
            type="button"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={HandleLogin}
          >
            登录
          </Button>
        </Box>
      </Box>
    </div>
  );
}
