---
type: Jurisdiction
title: "Stafford County, VA"
classification: county
fips: "51179"
state: "VA"
demographics:
  population: 168919
  population_under_18: 47878
  population_18_64: 58162
  population_65_plus: 62879
  median_household_income: 138093
  poverty_rate: 4.83
  homeownership_rate: 79.65
  unemployment_rate: 3.0
  median_home_value: 541300
  gini_index: 0.3723
  vacancy_rate: 2.85
  race_white: 85419
  race_black: 38009
  race_asian: 7131
  race_native: 530
  hispanic: 29991
  bachelors_plus: 70467
districts:
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.9972
  - to: "us/states/va/districts/senate/27"
    rel: in-district
    area_weight: 0.7242
  - to: "us/states/va/districts/senate/29"
    rel: in-district
    area_weight: 0.2711
  - to: "us/states/va/districts/house/64"
    rel: in-district
    area_weight: 0.4979
  - to: "us/states/va/districts/house/23"
    rel: in-district
    area_weight: 0.2645
  - to: "us/states/va/districts/house/65"
    rel: in-district
    area_weight: 0.2329
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Stafford County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 168919 |
| Under 18 | 47878 |
| 18–64 | 58162 |
| 65+ | 62879 |
| Median household income | 138093 |
| Poverty rate | 4.83 |
| Homeownership rate | 79.65 |
| Unemployment rate | 3.0 |
| Median home value | 541300 |
| Gini index | 0.3723 |
| Vacancy rate | 2.85 |
| White | 85419 |
| Black | 38009 |
| Asian | 7131 |
| Native | 530 |
| Hispanic/Latino | 29991 |
| Bachelor's or higher | 70467 |

## Districts

- [VA-07](/us/states/va/districts/07.md) — 100% (congressional)
- [VA Senate District 27](/us/states/va/districts/senate/27.md) — 72% (state senate)
- [VA Senate District 29](/us/states/va/districts/senate/29.md) — 27% (state senate)
- [VA House District 64](/us/states/va/districts/house/64.md) — 50% (state house)
- [VA House District 23](/us/states/va/districts/house/23.md) — 26% (state house)
- [VA House District 65](/us/states/va/districts/house/65.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
