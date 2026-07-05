---
type: Jurisdiction
title: "Lincoln County, WY"
classification: county
fips: "56023"
state: "WY"
demographics:
  population: 20486
  population_under_18: 5160
  population_18_64: 11407
  population_65_plus: 3919
  median_household_income: 89330
  poverty_rate: 7.46
  homeownership_rate: 77.03
  unemployment_rate: 2.02
  median_home_value: 372600
  gini_index: 0.4042
  vacancy_rate: 16.46
  race_white: 18878
  race_black: 10
  race_asian: 67
  race_native: 57
  hispanic: 1131
  bachelors_plus: 4744
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wy/districts/senate/14"
    rel: in-district
    area_weight: 0.6753
  - to: "us/states/wy/districts/senate/16"
    rel: in-district
    area_weight: 0.3246
  - to: "us/states/wy/districts/house/18"
    rel: in-district
    area_weight: 0.5706
  - to: "us/states/wy/districts/house/22"
    rel: in-district
    area_weight: 0.2094
  - to: "us/states/wy/districts/house/21"
    rel: in-district
    area_weight: 0.1151
  - to: "us/states/wy/districts/house/20"
    rel: in-district
    area_weight: 0.1046
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Lincoln County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20486 |
| Under 18 | 5160 |
| 18–64 | 11407 |
| 65+ | 3919 |
| Median household income | 89330 |
| Poverty rate | 7.46 |
| Homeownership rate | 77.03 |
| Unemployment rate | 2.02 |
| Median home value | 372600 |
| Gini index | 0.4042 |
| Vacancy rate | 16.46 |
| White | 18878 |
| Black | 10 |
| Asian | 67 |
| Native | 57 |
| Hispanic/Latino | 1131 |
| Bachelor's or higher | 4744 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 14](/us/states/wy/districts/senate/14.md) — 68% (state senate)
- [WY Senate District 16](/us/states/wy/districts/senate/16.md) — 32% (state senate)
- [WY House District 18](/us/states/wy/districts/house/18.md) — 57% (state house)
- [WY House District 22](/us/states/wy/districts/house/22.md) — 21% (state house)
- [WY House District 21](/us/states/wy/districts/house/21.md) — 12% (state house)
- [WY House District 20](/us/states/wy/districts/house/20.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
