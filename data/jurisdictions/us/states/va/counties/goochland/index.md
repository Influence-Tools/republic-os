---
type: Jurisdiction
title: "Goochland County, VA"
classification: county
fips: "51075"
state: "VA"
demographics:
  population: 26410
  population_under_18: 4272
  population_18_64: 15503
  population_65_plus: 6635
  median_household_income: 118931
  poverty_rate: 5.14
  homeownership_rate: 84.94
  unemployment_rate: 1.66
  median_home_value: 500600
  gini_index: 0.4654
  vacancy_rate: 7.73
  race_white: 20703
  race_black: 3611
  race_asian: 501
  race_native: 16
  hispanic: 1004
  bachelors_plus: 13312
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/56"
    rel: in-district
    area_weight: 0.8262
  - to: "us/states/va/districts/house/57"
    rel: in-district
    area_weight: 0.173
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Goochland County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26410 |
| Under 18 | 4272 |
| 18–64 | 15503 |
| 65+ | 6635 |
| Median household income | 118931 |
| Poverty rate | 5.14 |
| Homeownership rate | 84.94 |
| Unemployment rate | 1.66 |
| Median home value | 500600 |
| Gini index | 0.4654 |
| Vacancy rate | 7.73 |
| White | 20703 |
| Black | 3611 |
| Asian | 501 |
| Native | 16 |
| Hispanic/Latino | 1004 |
| Bachelor's or higher | 13312 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 100% (state senate)
- [VA House District 56](/us/states/va/districts/house/56.md) — 83% (state house)
- [VA House District 57](/us/states/va/districts/house/57.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
