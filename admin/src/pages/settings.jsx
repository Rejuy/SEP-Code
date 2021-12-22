import { Button, Dialog, DialogContent, DialogTitle } from "@mui/material";
import React from "react";
import { useNavigate } from "react-router-dom";

export default function SettingsPage(props) {
  const { open, handleClose } = props;
  const navigate = useNavigate();

  const logout = () => {
    handleClose();
    localStorage.setItem("secretCode", "");
    navigate("/login");
  };

  return (
    <Dialog open={open} onClose={handleClose} fullWidth>
      <DialogTitle style={{ display: "flex", justifyContent: "center" }}>
        设置
      </DialogTitle>
      <DialogContent>
        <Button variant="outlined" color="error" onClick={logout} fullWidth>
          登出
        </Button>
      </DialogContent>
    </Dialog>
  );
}
