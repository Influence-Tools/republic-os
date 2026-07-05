---
type: Jurisdiction
title: "Juneau City and Borough, AK"
classification: county
fips: "02110"
state: "AK"
demographics:
  population: 31794
  population_under_18: 7331
  population_18_64: 10944
  population_65_plus: 13519
  median_household_income: 101661
  poverty_rate: 8.91
  homeownership_rate: 63.61
  unemployment_rate: 4.01
  median_home_value: 449300
  gini_index: 0.4237
  vacancy_rate: 7.59
  race_white: 19888
  race_black: 226
  race_asian: 2383
  race_native: 2786
  hispanic: 2245
  bachelors_plus: 12922
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.8761
  - to: "us/states/ak/districts/senate/b"
    rel: in-district
    area_weight: 0.8628
  - to: "us/states/ak/districts/house/4"
    rel: in-district
    area_weight: 0.6558
  - to: "us/states/ak/districts/house/3"
    rel: in-district
    area_weight: 0.207
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Juneau City and Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31794 |
| Under 18 | 7331 |
| 18–64 | 10944 |
| 65+ | 13519 |
| Median household income | 101661 |
| Poverty rate | 8.91 |
| Homeownership rate | 63.61 |
| Unemployment rate | 4.01 |
| Median home value | 449300 |
| Gini index | 0.4237 |
| Vacancy rate | 7.59 |
| White | 19888 |
| Black | 226 |
| Asian | 2383 |
| Native | 2786 |
| Hispanic/Latino | 2245 |
| Bachelor's or higher | 12922 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 88% (congressional)
- [AK Senate District B](/us/states/ak/districts/senate/b.md) — 86% (state senate)
- [AK House District 4](/us/states/ak/districts/house/4.md) — 66% (state house)
- [AK House District 3](/us/states/ak/districts/house/3.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
