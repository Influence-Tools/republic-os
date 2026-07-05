---
type: Jurisdiction
title: "Jessamine County, KY"
classification: county
fips: "21113"
state: "KY"
demographics:
  population: 54588
  population_under_18: 12966
  population_18_64: 32744
  population_65_plus: 8878
  median_household_income: 74576
  poverty_rate: 11.27
  homeownership_rate: 66.75
  unemployment_rate: 3.13
  median_home_value: 268100
  gini_index: 0.5163
  vacancy_rate: 6.06
  race_white: 47486
  race_black: 2221
  race_asian: 979
  race_native: 50
  hispanic: 2740
  bachelors_plus: 17610
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/22"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/55"
    rel: in-district
    area_weight: 0.4325
  - to: "us/states/ky/districts/house/39"
    rel: in-district
    area_weight: 0.2682
  - to: "us/states/ky/districts/house/56"
    rel: in-district
    area_weight: 0.1533
  - to: "us/states/ky/districts/house/45"
    rel: in-district
    area_weight: 0.1456
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Jessamine County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54588 |
| Under 18 | 12966 |
| 18–64 | 32744 |
| 65+ | 8878 |
| Median household income | 74576 |
| Poverty rate | 11.27 |
| Homeownership rate | 66.75 |
| Unemployment rate | 3.13 |
| Median home value | 268100 |
| Gini index | 0.5163 |
| Vacancy rate | 6.06 |
| White | 47486 |
| Black | 2221 |
| Asian | 979 |
| Native | 50 |
| Hispanic/Latino | 2740 |
| Bachelor's or higher | 17610 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 100% (congressional)
- [KY Senate District 22](/us/states/ky/districts/senate/22.md) — 100% (state senate)
- [KY House District 55](/us/states/ky/districts/house/55.md) — 43% (state house)
- [KY House District 39](/us/states/ky/districts/house/39.md) — 27% (state house)
- [KY House District 56](/us/states/ky/districts/house/56.md) — 15% (state house)
- [KY House District 45](/us/states/ky/districts/house/45.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
