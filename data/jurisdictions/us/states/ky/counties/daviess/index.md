---
type: Jurisdiction
title: "Daviess County, KY"
classification: county
fips: "21059"
state: "KY"
demographics:
  population: 103648
  population_under_18: 25381
  population_18_64: 59947
  population_65_plus: 18320
  median_household_income: 68214
  poverty_rate: 14.72
  homeownership_rate: 68.06
  unemployment_rate: 4.45
  median_home_value: 199900
  gini_index: 0.467
  vacancy_rate: 6.28
  race_white: 88857
  race_black: 4285
  race_asian: 2173
  race_native: 505
  hispanic: 4412
  bachelors_plus: 25775
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/ky/districts/senate/8"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/7"
    rel: in-district
    area_weight: 0.4815
  - to: "us/states/ky/districts/house/14"
    rel: in-district
    area_weight: 0.3994
  - to: "us/states/ky/districts/house/13"
    rel: in-district
    area_weight: 0.1189
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Daviess County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 103648 |
| Under 18 | 25381 |
| 18–64 | 59947 |
| 65+ | 18320 |
| Median household income | 68214 |
| Poverty rate | 14.72 |
| Homeownership rate | 68.06 |
| Unemployment rate | 4.45 |
| Median home value | 199900 |
| Gini index | 0.467 |
| Vacancy rate | 6.28 |
| White | 88857 |
| Black | 4285 |
| Asian | 2173 |
| Native | 505 |
| Hispanic/Latino | 4412 |
| Bachelor's or higher | 25775 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 8](/us/states/ky/districts/senate/8.md) — 100% (state senate)
- [KY House District 7](/us/states/ky/districts/house/7.md) — 48% (state house)
- [KY House District 14](/us/states/ky/districts/house/14.md) — 40% (state house)
- [KY House District 13](/us/states/ky/districts/house/13.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
