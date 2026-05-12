const DashboardCard = ({
  title,
  value,
}: {
  title: string;
  value: any;
}) => {

  return (

    <div
      style={{
        background: "white",
        borderRadius: "16px",
        padding: "24px",
        width: "240px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.08)",
      }}
    >

      <h3
        style={{
          color: "#6b7280",
          marginBottom: "10px",
        }}
      >
        {title}
      </h3>

      <h1>
        {value}
      </h1>

    </div>
  );
};

export default DashboardCard;