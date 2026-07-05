---
type: Jurisdiction
title: "Santa Clara County, CA"
classification: county
fips: "06085"
state: "CA"
demographics:
  population: 1902047
  population_under_18: 390076
  population_18_64: 1229961
  population_65_plus: 282010
  median_household_income: 164281
  poverty_rate: 7.11
  homeownership_rate: 55.08
  unemployment_rate: 4.87
  median_home_value: 1490600
  gini_index: 0.4764
  vacancy_rate: 5.65
  race_white: 568135
  race_black: 43917
  race_asian: 770311
  race_native: 16500
  hispanic: 475827
  bachelors_plus: 1142708
districts:
  - to: "us/states/ca/districts/18"
    rel: in-district
    area_weight: 0.5755
  - to: "us/states/ca/districts/19"
    rel: in-district
    area_weight: 0.1748
  - to: "us/states/ca/districts/16"
    rel: in-district
    area_weight: 0.1461
  - to: "us/states/ca/districts/17"
    rel: in-district
    area_weight: 0.0977
  - to: "us/states/ca/districts/senate/15"
    rel: in-district
    area_weight: 0.8029
  - to: "us/states/ca/districts/senate/13"
    rel: in-district
    area_weight: 0.1121
  - to: "us/states/ca/districts/senate/10"
    rel: in-district
    area_weight: 0.0817
  - to: "us/states/ca/districts/house/25"
    rel: in-district
    area_weight: 0.5376
  - to: "us/states/ca/districts/house/28"
    rel: in-district
    area_weight: 0.1973
  - to: "us/states/ca/districts/house/23"
    rel: in-district
    area_weight: 0.0953
  - to: "us/states/ca/districts/house/29"
    rel: in-district
    area_weight: 0.0688
  - to: "us/states/ca/districts/house/26"
    rel: in-district
    area_weight: 0.0629
  - to: "us/states/ca/districts/house/24"
    rel: in-district
    area_weight: 0.035
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Santa Clara County, CA

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1902047 |
| Under 18 | 390076 |
| 18–64 | 1229961 |
| 65+ | 282010 |
| Median household income | 164281 |
| Poverty rate | 7.11 |
| Homeownership rate | 55.08 |
| Unemployment rate | 4.87 |
| Median home value | 1490600 |
| Gini index | 0.4764 |
| Vacancy rate | 5.65 |
| White | 568135 |
| Black | 43917 |
| Asian | 770311 |
| Native | 16500 |
| Hispanic/Latino | 475827 |
| Bachelor's or higher | 1142708 |

## Districts

- [CA-18](/us/states/ca/districts/18.md) — 58% (congressional)
- [CA-19](/us/states/ca/districts/19.md) — 17% (congressional)
- [CA-16](/us/states/ca/districts/16.md) — 15% (congressional)
- [CA-17](/us/states/ca/districts/17.md) — 10% (congressional)
- [CA Senate District 15](/us/states/ca/districts/senate/15.md) — 80% (state senate)
- [CA Senate District 13](/us/states/ca/districts/senate/13.md) — 11% (state senate)
- [CA Senate District 10](/us/states/ca/districts/senate/10.md) — 8% (state senate)
- [CA House District 25](/us/states/ca/districts/house/25.md) — 54% (state house)
- [CA House District 28](/us/states/ca/districts/house/28.md) — 20% (state house)
- [CA House District 23](/us/states/ca/districts/house/23.md) — 10% (state house)
- [CA House District 29](/us/states/ca/districts/house/29.md) — 7% (state house)
- [CA House District 26](/us/states/ca/districts/house/26.md) — 6% (state house)
- [CA House District 24](/us/states/ca/districts/house/24.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
