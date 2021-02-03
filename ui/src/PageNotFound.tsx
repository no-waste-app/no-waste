import { useTranslation } from "react-i18next";

export function PageNotFound(): JSX.Element {
  const { t } = useTranslation();

  return <div>{t("common.notFound")}</div>;
}
