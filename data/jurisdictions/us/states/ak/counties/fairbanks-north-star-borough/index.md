---
type: Jurisdiction
title: "Fairbanks North Star Borough, AK"
classification: county
fips: "02090"
state: "AK"
demographics:
  population: 94951
  population_under_18: 24311
  population_18_64: 39353
  population_65_plus: 31287
  median_household_income: 92121
  poverty_rate: 4.98
  homeownership_rate: 64.68
  unemployment_rate: 5.68
  median_home_value: 329200
  gini_index: 0.403
  vacancy_rate: 14.9
  race_white: 63632
  race_black: 3574
  race_asian: 3316
  race_native: 7072
  hispanic: 8742
  bachelors_plus: 29569
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ak/districts/senate/q"
    rel: in-district
    area_weight: 0.5764
  - to: "us/states/ak/districts/senate/r"
    rel: in-district
    area_weight: 0.4168
  - to: "us/states/ak/districts/senate/p"
    rel: in-district
    area_weight: 0.0069
  - to: "us/states/ak/districts/house/34"
    rel: in-district
    area_weight: 0.561
  - to: "us/states/ak/districts/house/36"
    rel: in-district
    area_weight: 0.2138
  - to: "us/states/ak/districts/house/35"
    rel: in-district
    area_weight: 0.2029
  - to: "us/states/ak/districts/house/33"
    rel: in-district
    area_weight: 0.0153
  - to: "us/states/ak/districts/house/32"
    rel: in-district
    area_weight: 0.0055
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Fairbanks North Star Borough, AK

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 94951 |
| Under 18 | 24311 |
| 18–64 | 39353 |
| 65+ | 31287 |
| Median household income | 92121 |
| Poverty rate | 4.98 |
| Homeownership rate | 64.68 |
| Unemployment rate | 5.68 |
| Median home value | 329200 |
| Gini index | 0.403 |
| Vacancy rate | 14.9 |
| White | 63632 |
| Black | 3574 |
| Asian | 3316 |
| Native | 7072 |
| Hispanic/Latino | 8742 |
| Bachelor's or higher | 29569 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 100% (congressional)
- [AK Senate District Q](/us/states/ak/districts/senate/q.md) — 58% (state senate)
- [AK Senate District R](/us/states/ak/districts/senate/r.md) — 42% (state senate)
- [AK Senate District P](/us/states/ak/districts/senate/p.md) — 1% (state senate)
- [AK House District 34](/us/states/ak/districts/house/34.md) — 56% (state house)
- [AK House District 36](/us/states/ak/districts/house/36.md) — 21% (state house)
- [AK House District 35](/us/states/ak/districts/house/35.md) — 20% (state house)
- [AK House District 33](/us/states/ak/districts/house/33.md) — 2% (state house)
- [AK House District 32](/us/states/ak/districts/house/32.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
