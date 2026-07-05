---
type: Jurisdiction
title: "Loudoun County, VA"
classification: county
fips: "51107"
state: "VA"
demographics:
  population: 432998
  population_under_18: 115171
  population_18_64: 270933
  population_65_plus: 46894
  median_household_income: 181765
  poverty_rate: 4.23
  homeownership_rate: 77.91
  unemployment_rate: 3.31
  median_home_value: 743800
  gini_index: 0.3908
  vacancy_rate: 2.7
  race_white: 228302
  race_black: 33411
  race_asian: 94508
  race_native: 1253
  hispanic: 61750
  bachelors_plus: 264511
districts:
  - to: "us/states/va/districts/10"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/va/districts/senate/31"
    rel: in-district
    area_weight: 0.8239
  - to: "us/states/va/districts/senate/32"
    rel: in-district
    area_weight: 0.1752
  - to: "us/states/va/districts/house/30"
    rel: in-district
    area_weight: 0.7266
  - to: "us/states/va/districts/house/29"
    rel: in-district
    area_weight: 0.0924
  - to: "us/states/va/districts/house/27"
    rel: in-district
    area_weight: 0.0732
  - to: "us/states/va/districts/house/28"
    rel: in-district
    area_weight: 0.0541
  - to: "us/states/va/districts/house/26"
    rel: in-district
    area_weight: 0.0528
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Loudoun County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 432998 |
| Under 18 | 115171 |
| 18–64 | 270933 |
| 65+ | 46894 |
| Median household income | 181765 |
| Poverty rate | 4.23 |
| Homeownership rate | 77.91 |
| Unemployment rate | 3.31 |
| Median home value | 743800 |
| Gini index | 0.3908 |
| Vacancy rate | 2.7 |
| White | 228302 |
| Black | 33411 |
| Asian | 94508 |
| Native | 1253 |
| Hispanic/Latino | 61750 |
| Bachelor's or higher | 264511 |

## Districts

- [VA-10](/us/states/va/districts/10.md) — 100% (congressional)
- [VA Senate District 31](/us/states/va/districts/senate/31.md) — 82% (state senate)
- [VA Senate District 32](/us/states/va/districts/senate/32.md) — 18% (state senate)
- [VA House District 30](/us/states/va/districts/house/30.md) — 73% (state house)
- [VA House District 29](/us/states/va/districts/house/29.md) — 9% (state house)
- [VA House District 27](/us/states/va/districts/house/27.md) — 7% (state house)
- [VA House District 28](/us/states/va/districts/house/28.md) — 5% (state house)
- [VA House District 26](/us/states/va/districts/house/26.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
