---
type: Jurisdiction
title: "St. Johns County, FL"
classification: county
fips: "12109"
state: "FL"
demographics:
  population: 306934
  population_under_18: 66193
  population_18_64: 176124
  population_65_plus: 64617
  median_household_income: 109839
  poverty_rate: 6.54
  homeownership_rate: 82.23
  unemployment_rate: 3.31
  median_home_value: 489200
  gini_index: 0.4555
  vacancy_rate: 13.27
  race_white: 243237
  race_black: 15694
  race_asian: 11538
  race_native: 266
  hispanic: 27846
  bachelors_plus: 154674
districts:
  - to: "us/states/fl/districts/05"
    rel: in-district
    area_weight: 0.5056
  - to: "us/states/fl/districts/06"
    rel: in-district
    area_weight: 0.3135
  - to: "us/states/fl/districts/senate/7"
    rel: in-district
    area_weight: 0.8196
  - to: "us/states/fl/districts/house/20"
    rel: in-district
    area_weight: 0.3623
  - to: "us/states/fl/districts/house/18"
    rel: in-district
    area_weight: 0.3613
  - to: "us/states/fl/districts/house/19"
    rel: in-district
    area_weight: 0.0961
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# St. Johns County, FL

County jurisdiction — 28 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 306934 |
| Under 18 | 66193 |
| 18–64 | 176124 |
| 65+ | 64617 |
| Median household income | 109839 |
| Poverty rate | 6.54 |
| Homeownership rate | 82.23 |
| Unemployment rate | 3.31 |
| Median home value | 489200 |
| Gini index | 0.4555 |
| Vacancy rate | 13.27 |
| White | 243237 |
| Black | 15694 |
| Asian | 11538 |
| Native | 266 |
| Hispanic/Latino | 27846 |
| Bachelor's or higher | 154674 |

## Districts

- [FL-05](/us/states/fl/districts/05.md) — 51% (congressional)
- [FL-06](/us/states/fl/districts/06.md) — 31% (congressional)
- [FL Senate District 7](/us/states/fl/districts/senate/7.md) — 82% (state senate)
- [FL House District 20](/us/states/fl/districts/house/20.md) — 36% (state house)
- [FL House District 18](/us/states/fl/districts/house/18.md) — 36% (state house)
- [FL House District 19](/us/states/fl/districts/house/19.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
