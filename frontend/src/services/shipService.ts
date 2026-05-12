import api from "../api/axios";

export const getShips = async () => {

  const response = await api.get(
    "ships/"
  );

  return response.data;
};