---
type: Jurisdiction
title: "Fayette County, GA"
classification: county
fips: "13113"
state: "GA"
demographics:
  population: 122244
  population_under_18: 27500
  population_18_64: 70277
  population_65_plus: 24467
  median_household_income: 111978
  poverty_rate: 5.58
  homeownership_rate: 80.11
  unemployment_rate: 3.8
  median_home_value: 436400
  gini_index: 0.4386
  vacancy_rate: 4.03
  race_white: 69352
  race_black: 31267
  race_asian: 6085
  race_native: 235
  hispanic: 10504
  bachelors_plus: 58062
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.8366
  - to: "us/states/ga/districts/06"
    rel: in-district
    area_weight: 0.1579
  - to: "us/states/ga/districts/senate/16"
    rel: in-district
    area_weight: 0.7631
  - to: "us/states/ga/districts/senate/34"
    rel: in-district
    area_weight: 0.236
  - to: "us/states/ga/districts/house/82"
    rel: in-district
    area_weight: 0.3513
  - to: "us/states/ga/districts/house/69"
    rel: in-district
    area_weight: 0.2493
  - to: "us/states/ga/districts/house/68"
    rel: in-district
    area_weight: 0.2424
  - to: "us/states/ga/districts/house/73"
    rel: in-district
    area_weight: 0.1563
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Fayette County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 122244 |
| Under 18 | 27500 |
| 18–64 | 70277 |
| 65+ | 24467 |
| Median household income | 111978 |
| Poverty rate | 5.58 |
| Homeownership rate | 80.11 |
| Unemployment rate | 3.8 |
| Median home value | 436400 |
| Gini index | 0.4386 |
| Vacancy rate | 4.03 |
| White | 69352 |
| Black | 31267 |
| Asian | 6085 |
| Native | 235 |
| Hispanic/Latino | 10504 |
| Bachelor's or higher | 58062 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 84% (congressional)
- [GA-06](/us/states/ga/districts/06.md) — 16% (congressional)
- [GA Senate District 16](/us/states/ga/districts/senate/16.md) — 76% (state senate)
- [GA Senate District 34](/us/states/ga/districts/senate/34.md) — 24% (state senate)
- [GA House District 82](/us/states/ga/districts/house/82.md) — 35% (state house)
- [GA House District 69](/us/states/ga/districts/house/69.md) — 25% (state house)
- [GA House District 68](/us/states/ga/districts/house/68.md) — 24% (state house)
- [GA House District 73](/us/states/ga/districts/house/73.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
