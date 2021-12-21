import React, { useEffect, useState } from "react";
import {
  Button,
  Checkbox,
  CircularProgress,
  Container,
  FormControlLabel,
  FormGroup,
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

export default function Courseinfo() {
  const navigate = useNavigate();
  const { id } = useParams();
  const [loaded, setLoaded] = useState(false);
  const [data, setData] = useState({
    id: -1,
    name: "",
    teacher: "",
    department: 0,
    type: 0,
    credit: 0,
    time: "",
    activated: false,
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
      <Typography variant="h5">加载课程</Typography>
      <CircularProgress />
    </div>
  );

  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_single_item", {
        secret_code: localStorage.getItem("secretCode"),
        id: id,
        class: 1,
      })
      .then((res) => {
        setData(res.data.item);
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
            label="课程名称"
            variant="standard"
            value={data.name}
            onChange={(e) => {
              setData((prev) => ({ ...prev, name: e.target.value }));
            }}
          />
        </div>
        <div>
          <TextField
            required
            label="老师"
            variant="standard"
            value={data.teacher}
            onChange={(e) => {
              setData((prev) => ({ ...prev, teacher: e.target.value }));
            }}
          />
          <TextField
            required
            label="院系"
            variant="standard"
            value={data.department}
            onChange={(e) => {
              setData((prev) => ({
                ...prev,
                department: Number(e.target.value),
              }));
            }}
          />
        </div>
        <div>
          <TextField
            required
            label="类型"
            variant="standard"
            value={data.type}
            onChange={(e) => {
              setData((prev) => ({ ...prev, type: Number(e.target.value) }));
            }}
          />
          <TextField
            required
            label="学分"
            variant="standard"
            type="number"
            value={data.credit}
            onChange={(e) => {
              setData((prev) => ({ ...prev, credit: Number(e.target.value) }));
            }}
          />
        </div>
        <div style={{ display: "flex", alignItems: "center" }}>
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
          <FormGroup>
            <FormControlLabel
              control={
                <Checkbox
                  checked={data.activated === 1}
                  onChange={(e) => {
                    setData((prev) => ({
                      ...prev,
                      activated: e.target.checked ? 1 : 0,
                    }));
                  }}
                />
              }
              label="激活"
            />
          </FormGroup>
        </div>
        <div>
          <Button
            variant="outlined"
            color="success"
            fullWidth
            onClick={() => {
              console.log(data);
              axios
                .post(global.config.backendUrl + "/api/v1.0/admin_edit_item", {
                  secret_code: localStorage.getItem("secretCode"),
                  class: 1,
                  item: data,
                  delete: false,
                })
                .then((res) => {
                  navigate("/courses");
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
                .post(global.config.backendUrl + "/api/v1.0/admin_edit_item", {
                  secret_code: localStorage.getItem("secretCode"),
                  item: { id: data.id },
                  class: 1,
                  delete: true,
                })
                .then((res) => {
                  navigate("/courses");
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
              navigate("/courses");
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
