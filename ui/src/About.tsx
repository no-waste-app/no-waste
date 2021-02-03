import { useTranslation } from "react-i18next";

export function About(): JSX.Element {
  const { t } = useTranslation();

  return (
    <div>
      <h1>{t("aboutPage.about")}</h1>
    </div>
  );
}
