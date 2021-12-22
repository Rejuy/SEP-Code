import {
  Button,
  Card,
  CardActions,
  CardContent,
  Typography,
} from "@mui/material";
import axios from "axios";
import React, { Component } from "react";
import { Link } from "react-router-dom";
import "../../config";

export default class Timeonline extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  componentDidMount() {
    axios
      .post(global.config.backendUrl + "/api/v1.0/get_online_time", {
        secret_code: localStorage.getItem("secretCode"),
      })
      .then((res) => {
        this.setState({ count: (new Date() - new Date(res.data.date)) / 1000 });
        this.timerId = setInterval(() => {
          this.setState({ count: this.state.count + 1 });
        }, 1000);
      });
  }

  componentWillUnmount() {
    clearInterval(this.timerId);
  }

  render() {
    const count = this.state.count;
    return (
      <Card>
        <CardContent>
          <Typography variant="h6" component="div">
            服务器在线时长
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            上次重启
          </Typography>
          <div
            style={{
              display: "flex",
              alignItems: "baseline",
              justifyContent: "space-evenly",
            }}
          >
            <Typography sx={{ fontSize: 26 }} color="text.primary" gutterBottom>
              {Math.floor(count / 3600 / 60)} 天
            </Typography>
            <Typography sx={{ fontSize: 24 }} color="text.primary" gutterBottom>
              {Math.floor((count / 3600) % 60)} 小时
            </Typography>
            <Typography sx={{ fontSize: 20 }} gutterBottom>
              {Math.floor((count / 60) % 60)} 分
            </Typography>
            <Typography sx={{ fontSize: 16 }} gutterBottom>
              {Math.floor(count % 60)} 秒
            </Typography>
          </div>
        </CardContent>
        <CardActions>
          <Link to="/">
            <Button size="small">了解更多</Button>
          </Link>
        </CardActions>
      </Card>
    );
  }
}
