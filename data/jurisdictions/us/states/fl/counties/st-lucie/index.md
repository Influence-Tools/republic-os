---
type: Jurisdiction
title: "St. Lucie County, FL"
classification: county
fips: "12111"
state: "FL"
demographics:
  population: 360500
  population_under_18: 70901
  population_18_64: 201065
  population_65_plus: 88534
  median_household_income: 71457
  poverty_rate: 12.28
  homeownership_rate: 78.56
  unemployment_rate: 6.06
  median_home_value: 347300
  gini_index: 0.4402
  vacancy_rate: 14.17
  race_white: 205243
  race_black: 77974
  race_asian: 7097
  race_native: 2001
  hispanic: 78741
  bachelors_plus: 95485
districts:
  - to: "us/states/fl/districts/21"
    rel: in-district
    area_weight: 0.8935
  - to: "us/states/fl/districts/senate/29"
    rel: in-district
    area_weight: 0.7622
  - to: "us/states/fl/districts/senate/31"
    rel: in-district
    area_weight: 0.1267
  - to: "us/states/fl/districts/house/84"
    rel: in-district
    area_weight: 0.77
  - to: "us/states/fl/districts/house/85"
    rel: in-district
    area_weight: 0.1188
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# St. Lucie County, FL

County jurisdiction — 33 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 360500 |
| Under 18 | 70901 |
| 18–64 | 201065 |
| 65+ | 88534 |
| Median household income | 71457 |
| Poverty rate | 12.28 |
| Homeownership rate | 78.56 |
| Unemployment rate | 6.06 |
| Median home value | 347300 |
| Gini index | 0.4402 |
| Vacancy rate | 14.17 |
| White | 205243 |
| Black | 77974 |
| Asian | 7097 |
| Native | 2001 |
| Hispanic/Latino | 78741 |
| Bachelor's or higher | 95485 |

## Districts

- [FL-21](/us/states/fl/districts/21.md) — 89% (congressional)
- [FL Senate District 29](/us/states/fl/districts/senate/29.md) — 76% (state senate)
- [FL Senate District 31](/us/states/fl/districts/senate/31.md) — 13% (state senate)
- [FL House District 84](/us/states/fl/districts/house/84.md) — 77% (state house)
- [FL House District 85](/us/states/fl/districts/house/85.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
