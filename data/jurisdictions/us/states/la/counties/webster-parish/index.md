---
type: Jurisdiction
title: "Webster Parish, LA"
classification: county
fips: "22119"
state: "LA"
demographics:
  population: 35820
  population_under_18: 8108
  population_18_64: 20301
  population_65_plus: 7411
  median_household_income: 41182
  poverty_rate: 23.13
  homeownership_rate: 66.84
  unemployment_rate: 5.15
  median_home_value: 114500
  gini_index: 0.4974
  vacancy_rate: 22.0
  race_white: 22192
  race_black: 12045
  race_asian: 97
  race_native: 120
  hispanic: 841
  bachelors_plus: 4281
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/la/districts/senate/36"
    rel: in-district
    area_weight: 0.5463
  - to: "us/states/la/districts/senate/33"
    rel: in-district
    area_weight: 0.2749
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 0.1787
  - to: "us/states/la/districts/house/10"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Webster Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 35820 |
| Under 18 | 8108 |
| 18–64 | 20301 |
| 65+ | 7411 |
| Median household income | 41182 |
| Poverty rate | 23.13 |
| Homeownership rate | 66.84 |
| Unemployment rate | 5.15 |
| Median home value | 114500 |
| Gini index | 0.4974 |
| Vacancy rate | 22.0 |
| White | 22192 |
| Black | 12045 |
| Asian | 97 |
| Native | 120 |
| Hispanic/Latino | 841 |
| Bachelor's or higher | 4281 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 36](/us/states/la/districts/senate/36.md) — 55% (state senate)
- [LA Senate District 33](/us/states/la/districts/senate/33.md) — 27% (state senate)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 18% (state senate)
- [LA House District 10](/us/states/la/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
