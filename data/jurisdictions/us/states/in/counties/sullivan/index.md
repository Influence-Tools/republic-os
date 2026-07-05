---
type: Jurisdiction
title: "Sullivan County, IN"
classification: county
fips: "18153"
state: "IN"
demographics:
  population: 20780
  population_under_18: 3907
  population_18_64: 12936
  population_65_plus: 3937
  median_household_income: 56204
  poverty_rate: 13.85
  homeownership_rate: 76.39
  unemployment_rate: 4.45
  median_home_value: 131100
  gini_index: 0.4442
  vacancy_rate: 10.91
  race_white: 18839
  race_black: 625
  race_asian: 80
  race_native: 17
  hispanic: 393
  bachelors_plus: 2849
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 0.9926
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.0074
  - to: "us/states/in/districts/senate/39"
    rel: in-district
    area_weight: 0.8249
  - to: "us/states/in/districts/senate/38"
    rel: in-district
    area_weight: 0.1748
  - to: "us/states/in/districts/house/45"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Sullivan County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20780 |
| Under 18 | 3907 |
| 18–64 | 12936 |
| 65+ | 3937 |
| Median household income | 56204 |
| Poverty rate | 13.85 |
| Homeownership rate | 76.39 |
| Unemployment rate | 4.45 |
| Median home value | 131100 |
| Gini index | 0.4442 |
| Vacancy rate | 10.91 |
| White | 18839 |
| Black | 625 |
| Asian | 80 |
| Native | 17 |
| Hispanic/Latino | 393 |
| Bachelor's or higher | 2849 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 99% (congressional)
- [IL-12](/us/states/il/districts/12.md) — 1% (congressional)
- [IN Senate District 39](/us/states/in/districts/senate/39.md) — 82% (state senate)
- [IN Senate District 38](/us/states/in/districts/senate/38.md) — 17% (state senate)
- [IN House District 45](/us/states/in/districts/house/45.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
