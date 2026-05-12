import api from "../api/axios";

export const loginUser = async (
  username: string,
  password: string
) => {

  const response = await api.post(
    "token/",
    {
      username,
      password,
    }
  );

  return response.data;
};