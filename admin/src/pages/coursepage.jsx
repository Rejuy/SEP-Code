import { styled, Container, Typography } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import React from "react";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
}));

function Coursepage() {
  const rows = [
    { id: 1, lastName: "Snow", firstName: "Jon", age: 35, activated: false },
    {
      id: 2,
      lastName: "Lannister",
      firstName: "Cersei",
      age: 42,
      activated: true,
    },
    {
      id: 3,
      lastName: "Lannister",
      firstName: "Jaime",
      age: 45,
      activated: true,
    },
    { id: 4, lastName: "Stark", firstName: "Arya", age: 16, activated: true },
    {
      id: 5,
      lastName: "Targaryen",
      firstName: "Daenerys",
      age: null,
      activated: true,
    },
    {
      id: 6,
      lastName: "Melisandre",
      firstName: null,
      age: 150,
      activated: false,
    },
    {
      id: 7,
      lastName: "Clifford",
      firstName: "Ferrara",
      age: 44,
      activated: false,
    },
    {
      id: 8,
      lastName: "Frances",
      firstName: "Rossini",
      age: 36,
      activated: true,
    },
    { id: 9, lastName: "Roxie", firstName: "Harvey", age: 65, activated: true },
  ];
  const columns = [
    { field: "id", headerName: "ID", width: 70 },
    { field: "firstName", headerName: "First name", width: 130 },
    { field: "lastName", headerName: "Last name", width: 130 },
    {
      field: "age",
      headerName: "Age",
      type: "number",
      width: 90,
    },
    {
      field: "fullName",
      headerName: "Full name",
      description: "This column has a value getter and is not sortable.",
      sortable: false,
      width: 160,
      valueGetter: (params) =>
        `${params.getValue(params.id, "firstName") || ""} ${
          params.getValue(params.id, "lastName") || ""
        }`,
    },
    {
      field: "activated",
      headerName: "Account Active",
      width: 100,
      valueGetter: (params) => "a",
    },
  ];
  return (
    <CustomContainer>
      <Typography variant="h5" style={{ marginBottom: "20px" }}>
        Courses
      </Typography>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
      />
    </CustomContainer>
  );
}

export default Coursepage;
