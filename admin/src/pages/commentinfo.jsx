import React, { useEffect, useState } from "react";
import {
  Button,
  CircularProgress,
  Container,
  Rating,
  styled,
  TextField,
  Typography,
} from "@mui/material";
import AdapterDateFns from "@mui/lab/AdapterDateFns";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import "../config";
import { Box } from "@mui/system";
import { DesktopDatePicker, LocalizationProvider } from "@mui/lab";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
}));

export default function Commentinfo() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [loaded, setLoaded] = useState(false);
  const [data, setData] = useState({
    id: -1,
    class: "",
    item_id: -1,
    user: "",
    user_id: -1,
    star: 0,
    likes: 0,
    text: "",
    time: "",
  });
  const [dataJsx, setDataJsx] = useState(<></>);
  const loadingJsx = (
    <div
      className="loading"
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "space-evenly",
      }}
    >
      <Typography variant="h5">加载评论</Typography>
      <CircularProgress />
    </div>
  );

  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_single_comment", {
        secret_code: localStorage.getItem("secretCode"),
        id: id,
      })
      .then((res) => {
        setData(res.data.comment);
        setLoaded(true);
      })
      .catch((err) => console.log(err));
  }, [id]);

  useEffect(() => {
    setDataJsx(
      <Box
        sx={{
          "& .MuiTextField-root": { m: 1, width: "25ch" },
        }}
        noValidate
        autoComplete="off"
      >
        <div>
          <TextField
            InputProps={{
              readOnly: true,
            }}
            label="Id"
            variant="standard"
            value={data.id}
          />
          <TextField
            required
            label="Class"
            variant="standard"
            value={data.class}
            onChange={(e) => {
              setData((prev) => ({ ...prev, class: e.target.value }));
            }}
          />
        </div>
        <div>
          <TextField
            required
            label="Item Id"
            variant="standard"
            type="number"
            value={data.item_id}
            onChange={(e) => {
              setData((prev) => ({ ...prev, item_id: e.target.value }));
            }}
          />
          <TextField
            required
            label="User Id"
            variant="standard"
            type="number"
            value={data.user_id}
            onChange={(e) => {
              setData((prev) => ({
                ...prev,
                user_id: Number(e.target.value),
              }));
            }}
          />
        </div>
        <div>
          <TextField
            required
            label="Likes"
            variant="standard"
            type="number"
            value={data.likes}
            onChange={(e) => {
              setData((prev) => ({ ...prev, likes: e.target.value }));
            }}
          />
          <TextField
            required
            label="Text"
            variant="standard"
            value={data.text}
            onChange={(e) => {
              setData((prev) => ({
                ...prev,
                text: e.target.value,
              }));
            }}
          />
        </div>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div>
            <Typography component="legend">Rating</Typography>
            <Rating
              label="Rating"
              variant="standard"
              value={data.star}
              onChange={(e) => {
                setData((prev) => ({ ...prev, star: e.target.value }));
              }}
            />
          </div>
          <LocalizationProvider dateAdapter={AdapterDateFns}>
            <DesktopDatePicker
              label="时间"
              inputFormat="dd/MM/yyyy"
              variant="standard"
              value={data.time}
              onChange={(e) => {
                setData((prev) => ({
                  ...prev,
                  time: e.toLocaleDateString("zh-Hans-CN"),
                }));
              }}
              renderInput={(params) => <TextField {...params} />}
            />
          </LocalizationProvider>
        </div>
        <div>
          <Button
            variant="outlined"
            color="success"
            fullWidth
            onClick={() => {
              axios
                .post(
                  global.config.backendUrl + "/api/v1.0/admin_edit_comment",
                  {
                    secret_code: localStorage.getItem("secretCode"),
                    comment: data,
                    delete: false,
                  }
                )
                .then((res) => {
                  navigate("/comments");
                });
            }}
          >
            修改
          </Button>
        </div>
        <div style={{ marginTop: "10px" }}>
          <Button
            variant="outlined"
            color="error"
            fullWidth
            onClick={() => {
              axios
                .post(
                  global.config.backendUrl + "/api/v1.0/admin_edit_comment",
                  {
                    secret_code: localStorage.getItem("secretCode"),
                    comment: { id: data.id },
                    delete: true,
                  }
                )
                .then((res) => {
                  navigate("/comments");
                });
            }}
          >
            删除
          </Button>
        </div>
        <div style={{ marginTop: "10px" }}>
          <Button
            variant="outlined"
            color="primary"
            fullWidth
            onClick={() => {
              navigate("/comments");
            }}
          >
            返回
          </Button>
        </div>
      </Box>
    );
  }, [data, navigate]);

  return (
    <CustomContainer
      style={{ display: "flex", justifyContent: "space-evenly" }}
    >
      {loaded ? dataJsx : loadingJsx}
    </CustomContainer>
  );
}
