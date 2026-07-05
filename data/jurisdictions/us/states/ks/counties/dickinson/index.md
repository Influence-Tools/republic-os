---
type: Jurisdiction
title: "Dickinson County, KS"
classification: county
fips: "20041"
state: "KS"
demographics:
  population: 18445
  population_under_18: 4283
  population_18_64: 10272
  population_65_plus: 3890
  median_household_income: 68417
  poverty_rate: 8.14
  homeownership_rate: 78.57
  unemployment_rate: 2.76
  median_home_value: 146800
  gini_index: 0.4039
  vacancy_rate: 8.8
  race_white: 16722
  race_black: 18
  race_asian: 44
  race_native: 92
  hispanic: 1050
  bachelors_plus: 4080
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ks/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/70"
    rel: in-district
    area_weight: 0.8188
  - to: "us/states/ks/districts/house/64"
    rel: in-district
    area_weight: 0.1811
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Dickinson County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18445 |
| Under 18 | 4283 |
| 18–64 | 10272 |
| 65+ | 3890 |
| Median household income | 68417 |
| Poverty rate | 8.14 |
| Homeownership rate | 78.57 |
| Unemployment rate | 2.76 |
| Median home value | 146800 |
| Gini index | 0.4039 |
| Vacancy rate | 8.8 |
| White | 16722 |
| Black | 18 |
| Asian | 44 |
| Native | 92 |
| Hispanic/Latino | 1050 |
| Bachelor's or higher | 4080 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 24](/us/states/ks/districts/senate/24.md) — 100% (state senate)
- [KS House District 70](/us/states/ks/districts/house/70.md) — 82% (state house)
- [KS House District 64](/us/states/ks/districts/house/64.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
