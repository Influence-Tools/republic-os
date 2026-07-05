---
type: Jurisdiction
title: "Lewis and Clark County, MT"
classification: county
fips: "30049"
state: "MT"
demographics:
  population: 73464
  population_under_18: 15566
  population_18_64: 43055
  population_65_plus: 14843
  median_household_income: 78237
  poverty_rate: 8.06
  homeownership_rate: 70.08
  unemployment_rate: 3.24
  median_home_value: 393500
  gini_index: 0.4298
  vacancy_rate: 8.41
  race_white: 66597
  race_black: 417
  race_asian: 359
  race_native: 965
  hispanic: 2958
  bachelors_plus: 30194
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9977
  - to: "us/states/mt/districts/senate/9"
    rel: in-district
    area_weight: 0.79
  - to: "us/states/mt/districts/senate/42"
    rel: in-district
    area_weight: 0.106
  - to: "us/states/mt/districts/senate/40"
    rel: in-district
    area_weight: 0.0475
  - to: "us/states/mt/districts/senate/38"
    rel: in-district
    area_weight: 0.0441
  - to: "us/states/mt/districts/senate/41"
    rel: in-district
    area_weight: 0.0122
  - to: "us/states/mt/districts/house/17"
    rel: in-district
    area_weight: 0.79
  - to: "us/states/mt/districts/house/84"
    rel: in-district
    area_weight: 0.1019
  - to: "us/states/mt/districts/house/79"
    rel: in-district
    area_weight: 0.0457
  - to: "us/states/mt/districts/house/76"
    rel: in-district
    area_weight: 0.0441
  - to: "us/states/mt/districts/house/81"
    rel: in-district
    area_weight: 0.0084
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Lewis and Clark County, MT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 73464 |
| Under 18 | 15566 |
| 18–64 | 43055 |
| 65+ | 14843 |
| Median household income | 78237 |
| Poverty rate | 8.06 |
| Homeownership rate | 70.08 |
| Unemployment rate | 3.24 |
| Median home value | 393500 |
| Gini index | 0.4298 |
| Vacancy rate | 8.41 |
| White | 66597 |
| Black | 417 |
| Asian | 359 |
| Native | 965 |
| Hispanic/Latino | 2958 |
| Bachelor's or higher | 30194 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 9](/us/states/mt/districts/senate/9.md) — 79% (state senate)
- [MT Senate District 42](/us/states/mt/districts/senate/42.md) — 11% (state senate)
- [MT Senate District 40](/us/states/mt/districts/senate/40.md) — 5% (state senate)
- [MT Senate District 38](/us/states/mt/districts/senate/38.md) — 4% (state senate)
- [MT Senate District 41](/us/states/mt/districts/senate/41.md) — 1% (state senate)
- [MT House District 17](/us/states/mt/districts/house/17.md) — 79% (state house)
- [MT House District 84](/us/states/mt/districts/house/84.md) — 10% (state house)
- [MT House District 79](/us/states/mt/districts/house/79.md) — 5% (state house)
- [MT House District 76](/us/states/mt/districts/house/76.md) — 4% (state house)
- [MT House District 81](/us/states/mt/districts/house/81.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
