---
type: Jurisdiction
title: "Newport County, RI"
classification: county
fips: "44005"
state: "RI"
demographics:
  population: 84657
  population_under_18: 13551
  population_18_64: 49500
  population_65_plus: 21606
  median_household_income: 103514
  poverty_rate: 8.49
  homeownership_rate: 67.87
  unemployment_rate: 5.8
  median_home_value: 609700
  gini_index: 0.4646
  vacancy_rate: 15.56
  race_white: 70849
  race_black: 2916
  race_asian: 1448
  race_native: 171
  hispanic: 5701
  bachelors_plus: 49077
districts:
  - to: "us/states/ri/districts/01"
    rel: in-district
    area_weight: 0.3621
  - to: "us/states/ri/districts/senate/12"
    rel: in-district
    area_weight: 0.1843
  - to: "us/states/ri/districts/senate/11"
    rel: in-district
    area_weight: 0.0789
  - to: "us/states/ri/districts/senate/13"
    rel: in-district
    area_weight: 0.0562
  - to: "us/states/ri/districts/senate/10"
    rel: in-district
    area_weight: 0.0301
  - to: "us/states/ri/districts/house/71"
    rel: in-district
    area_weight: 0.1208
  - to: "us/states/ri/districts/house/70"
    rel: in-district
    area_weight: 0.0719
  - to: "us/states/ri/districts/house/72"
    rel: in-district
    area_weight: 0.0575
  - to: "us/states/ri/districts/house/74"
    rel: in-district
    area_weight: 0.0476
  - to: "us/states/ri/districts/house/69"
    rel: in-district
    area_weight: 0.0211
  - to: "us/states/ri/districts/house/75"
    rel: in-district
    area_weight: 0.0194
  - to: "us/states/ri/districts/house/73"
    rel: in-district
    area_weight: 0.0112
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ri]
timestamp: "2026-07-03"
---

# Newport County, RI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84657 |
| Under 18 | 13551 |
| 18–64 | 49500 |
| 65+ | 21606 |
| Median household income | 103514 |
| Poverty rate | 8.49 |
| Homeownership rate | 67.87 |
| Unemployment rate | 5.8 |
| Median home value | 609700 |
| Gini index | 0.4646 |
| Vacancy rate | 15.56 |
| White | 70849 |
| Black | 2916 |
| Asian | 1448 |
| Native | 171 |
| Hispanic/Latino | 5701 |
| Bachelor's or higher | 49077 |

## Districts

- [RI-01](/us/states/ri/districts/01.md) — 36% (congressional)
- [RI Senate District 12](/us/states/ri/districts/senate/12.md) — 18% (state senate)
- [RI Senate District 11](/us/states/ri/districts/senate/11.md) — 8% (state senate)
- [RI Senate District 13](/us/states/ri/districts/senate/13.md) — 6% (state senate)
- [RI Senate District 10](/us/states/ri/districts/senate/10.md) — 3% (state senate)
- [RI House District 71](/us/states/ri/districts/house/71.md) — 12% (state house)
- [RI House District 70](/us/states/ri/districts/house/70.md) — 7% (state house)
- [RI House District 72](/us/states/ri/districts/house/72.md) — 6% (state house)
- [RI House District 74](/us/states/ri/districts/house/74.md) — 5% (state house)
- [RI House District 69](/us/states/ri/districts/house/69.md) — 2% (state house)
- [RI House District 75](/us/states/ri/districts/house/75.md) — 2% (state house)
- [RI House District 73](/us/states/ri/districts/house/73.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
