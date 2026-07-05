---
type: Jurisdiction
title: "Rutherford County, NC"
classification: county
fips: "37161"
state: "NC"
demographics:
  population: 64930
  population_under_18: 13061
  population_18_64: 37411
  population_65_plus: 14458
  median_household_income: 51410
  poverty_rate: 16.75
  homeownership_rate: 73.88
  unemployment_rate: 6.35
  median_home_value: 201800
  gini_index: 0.4666
  vacancy_rate: 18.71
  race_white: 53155
  race_black: 4984
  race_asian: 304
  race_native: 145
  hispanic: 3698
  bachelors_plus: 14019
districts:
  - to: "us/states/nc/districts/14"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/nc/districts/senate/48"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/113"
    rel: in-district
    area_weight: 0.5446
  - to: "us/states/nc/districts/house/111"
    rel: in-district
    area_weight: 0.455
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Rutherford County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64930 |
| Under 18 | 13061 |
| 18–64 | 37411 |
| 65+ | 14458 |
| Median household income | 51410 |
| Poverty rate | 16.75 |
| Homeownership rate | 73.88 |
| Unemployment rate | 6.35 |
| Median home value | 201800 |
| Gini index | 0.4666 |
| Vacancy rate | 18.71 |
| White | 53155 |
| Black | 4984 |
| Asian | 304 |
| Native | 145 |
| Hispanic/Latino | 3698 |
| Bachelor's or higher | 14019 |

## Districts

- [NC-14](/us/states/nc/districts/14.md) — 100% (congressional)
- [NC Senate District 48](/us/states/nc/districts/senate/48.md) — 100% (state senate)
- [NC House District 113](/us/states/nc/districts/house/113.md) — 54% (state house)
- [NC House District 111](/us/states/nc/districts/house/111.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
