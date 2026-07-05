---
type: Jurisdiction
title: "Sweet Grass County, MT"
classification: county
fips: "30097"
state: "MT"
demographics:
  population: 3720
  population_under_18: 746
  population_18_64: 2015
  population_65_plus: 959
  median_household_income: 77000
  poverty_rate: 7.86
  homeownership_rate: 79.7
  unemployment_rate: 1.76
  median_home_value: 330100
  gini_index: 0.4565
  vacancy_rate: 18.32
  race_white: 3376
  race_black: 39
  race_asian: 7
  race_native: 63
  hispanic: 45
  bachelors_plus: 835
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/28"
    rel: in-district
    area_weight: 0.7394
  - to: "us/states/mt/districts/senate/39"
    rel: in-district
    area_weight: 0.2606
  - to: "us/states/mt/districts/house/56"
    rel: in-district
    area_weight: 0.7394
  - to: "us/states/mt/districts/house/78"
    rel: in-district
    area_weight: 0.2606
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Sweet Grass County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3720 |
| Under 18 | 746 |
| 18–64 | 2015 |
| 65+ | 959 |
| Median household income | 77000 |
| Poverty rate | 7.86 |
| Homeownership rate | 79.7 |
| Unemployment rate | 1.76 |
| Median home value | 330100 |
| Gini index | 0.4565 |
| Vacancy rate | 18.32 |
| White | 3376 |
| Black | 39 |
| Asian | 7 |
| Native | 63 |
| Hispanic/Latino | 45 |
| Bachelor's or higher | 835 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 28](/us/states/mt/districts/senate/28.md) — 74% (state senate)
- [MT Senate District 39](/us/states/mt/districts/senate/39.md) — 26% (state senate)
- [MT House District 56](/us/states/mt/districts/house/56.md) — 74% (state house)
- [MT House District 78](/us/states/mt/districts/house/78.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
