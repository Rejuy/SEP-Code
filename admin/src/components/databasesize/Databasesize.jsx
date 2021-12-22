import { Card, CardContent, Typography } from "@mui/material";
import axios from "axios";
import React, { useEffect, useState } from "react";
import "../../config";

export default function Databasesize() {
  const [count, setcount] = useState({
    total_length: 0,
    data_length: 0,
    index_length: 0,
  });
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_db_info", {
        secret_code: localStorage.getItem("secretCode"),
      })
      .then((res) => {
        setcount(res.data.info);
      });
  }, []);
  return (
    <Card>
      <CardContent>
        <Typography variant="h6" component="div">
          数据库大小
        </Typography>
        <span
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-evenly",
          }}
        >
          <Typography
            sx={{ fontSize: 20 }}
            color="text.secondary"
            style={{ display: "flex", alignItems: "baseline" }}
          >
            整体大小{" "}
            <Typography sx={{ fontSize: 30 }}>{count.total_length}</Typography>{" "}
            kB, 数据大小{" "}
            <Typography sx={{ fontSize: 30 }}>{count.data_length}</Typography>{" "}
            kB, 索引大小{" "}
            <Typography sx={{ fontSize: 30 }}>{count.index_length}</Typography>{" "}
            kB
          </Typography>
        </span>
      </CardContent>
    </Card>
  );
}
