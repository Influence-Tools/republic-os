---
type: Jurisdiction
title: "Walton County, GA"
classification: county
fips: "13297"
state: "GA"
demographics:
  population: 103313
  population_under_18: 24685
  population_18_64: 61779
  population_65_plus: 16849
  median_household_income: 84945
  poverty_rate: 11.93
  homeownership_rate: 79.27
  unemployment_rate: 5.33
  median_home_value: 339500
  gini_index: 0.4261
  vacancy_rate: 4.57
  race_white: 72260
  race_black: 19607
  race_asian: 1389
  race_native: 319
  hispanic: 6859
  bachelors_plus: 23422
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/senate/46"
    rel: in-district
    area_weight: 0.5809
  - to: "us/states/ga/districts/senate/42"
    rel: in-district
    area_weight: 0.4191
  - to: "us/states/ga/districts/house/112"
    rel: in-district
    area_weight: 0.5784
  - to: "us/states/ga/districts/house/114"
    rel: in-district
    area_weight: 0.233
  - to: "us/states/ga/districts/house/111"
    rel: in-district
    area_weight: 0.1882
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Walton County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 103313 |
| Under 18 | 24685 |
| 18–64 | 61779 |
| 65+ | 16849 |
| Median household income | 84945 |
| Poverty rate | 11.93 |
| Homeownership rate | 79.27 |
| Unemployment rate | 5.33 |
| Median home value | 339500 |
| Gini index | 0.4261 |
| Vacancy rate | 4.57 |
| White | 72260 |
| Black | 19607 |
| Asian | 1389 |
| Native | 319 |
| Hispanic/Latino | 6859 |
| Bachelor's or higher | 23422 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 46](/us/states/ga/districts/senate/46.md) — 58% (state senate)
- [GA Senate District 42](/us/states/ga/districts/senate/42.md) — 42% (state senate)
- [GA House District 112](/us/states/ga/districts/house/112.md) — 58% (state house)
- [GA House District 114](/us/states/ga/districts/house/114.md) — 23% (state house)
- [GA House District 111](/us/states/ga/districts/house/111.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
